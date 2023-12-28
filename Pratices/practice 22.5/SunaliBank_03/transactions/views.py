from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT, WITHDRAWAL,LOAN, LOAN_PAID, TRANSFER
from transactions.forms import (
    DepositForm,
    WithdrawForm,
    LoanRequestForm,
)
from django.views.generic.edit import FormView
from transactions.models import Transaction
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import MoneyTransferForm
from .models import Transaction, UserBankAccount, Account
from .constants import TRANSACTION_TYPE
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist 


def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # template e context data pass kora
        context.update({
            'title': self.title
        })

        return context

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        # if not account.initial_deposit_date:
        #     now = timezone.now()
        #     account.initial_deposit_date = now
        account.balance += amount # amount = 200, tar ager balance = 0 taka new balance = 0+200 = 200
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_transaction_email(self.request.user, amount, "Deposite Message", "transactions/deposite_email.html")
    #     mail_subject = "Deposit Message"
    #     message = render_to_string('transactions/deposite_email.html', {
    #     'user': self.request.user,
    #     'amount': amount
    # })

    # # Debug: Print rendered message
    #     print(message)

    #     to_email = self.request.user.email
    #     send_email = EmailMessage(mail_subject, message, to=[to_email])
    #     send_email.send()


def money_transfer_view(request):
    if request.method == 'POST':
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['balance']
            destination_username = form.cleaned_data['destination_username']
            
            # Retrieve user and destination account
            user = request.user
            destination_user = User.objects.get(username=destination_username)
            try:
                sender_account = request.user.account
            except ObjectDoesNotExist:
                messages.error(request, 'Your account does not exist.')
                return redirect('money_transfer')
            # Perform the transfer
            try:
                user_account = user.account
                destination_account = destination_user.account
            except Account.DoesNotExist:
                messages.error(request, 'Account not found. Transfer failed.')
                return redirect('money_transfer')

            if user_account.balance >= amount:
                user_account.balance -= amount
                user_account.save(update_fields=['balance'])
                
                destination_account.balance += amount
                destination_account.save(update_fields=['balance'])
                
                messages.success(request, f'Transfer successful! {amount}$ transferred to {destination_username}.')
            else:
                messages.error(request, 'Insufficient funds. Transfer failed.')
            return redirect('money_transfer')
    else:
        form = MoneyTransferForm()

    return render(request, 'transactions/money_transfer.html', {'form': form})

class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        
        self.request.user.account.balance -= form.cleaned_data.get('amount')
        # balance = 300
        # amount = 5000
        self.request.user.account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )
        send_transaction_email(self.request.user, amount, "Withdrawal Message", "transactions/withdrawal_email.html")
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(
            account=self.request.user.account,transaction_type=3,loan_approve=True).count()
        if current_loan_count >= 3:
            return HttpResponse("You have cross the loan limits")
        messages.success(
            self.request,
            f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
        )
        try:
            send_transaction_email(self.request.user, amount, "Loan Request Message", "transactions/loan_email.html")
        except Exception as e:
            print(f"Error sending email: {e}")
        
        return super().form_valid(form)
    
class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0 # filter korar pore ba age amar total balance ke show korbe
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            
            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
       
        return queryset.distinct() # unique queryset hote hobe
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context
    
        
class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        print(loan)
        if loan.loan_approve:
            user_account = loan.account
                # Reduce the loan amount from the user's balance
                # 5000, 500 + 5000 = 5500
                # balance = 3000, loan = 5000
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('transactions:loan_list')
            else:
                messages.error(
            self.request,
            f'Loan amount is greater than available balance'
        )

        return redirect('loan_list')


class LoanListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans' # loan list ta ei loans context er moddhe thakbe
    
    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account=user_account,transaction_type=3)
        print(queryset)
        return queryset
    
# class MoneyTransferView( FormView):
#     template_name = 'transactions/money_transfer.html'
#     form_class = MoneyTransferForm
#     success_url = reverse_lazy('money_transfer')  # Replace 'success' with the name of your success URL

#     def form_valid(self, form):
#         to_user_id = form.cleaned_data['to_user']
#         amount = form.cleaned_data['amount']

#         # Get the current user's account
#         from_account = self.request.user.account

#         try:
#             # Get the recipient's account
#             to_user = get_object_or_404(UserBankAccount, user__id=to_user_id)

#             # Check if the current user has enough balance for the transfer
#             if from_account.balance >= amount:
#                 # Perform the transfer
#                 from_account.balance -= amount
#                 from_account.save()

#                 to_user.balance += amount
#                 to_user.save()

#                 # Create transaction records
#                 Transaction.objects.create(
#                     account=from_account,
#                     to_user=to_user.user,
#                     amount=-amount,
#                     balance_after_transaction=from_account.balance,
#                     transaction_type=TRANSACTION_TYPE.DEBIT,
#                     loan_approve=False
#                 )

#                 Transaction.objects.create(
#                     account=to_user,
#                     to_user=from_account.user,
#                     amount=amount,
#                     balance_after_transaction=to_user.balance,
#                     transaction_type=TRANSACTION_TYPE.CREDIT,
#                     loan_approve=False
#                 )

#                 return super().form_valid(form)
#             else:
#                 form.add_error(None, 'Insufficient balance for the transfer.')
#                 return self.form_invalid(form)
#         except UserBankAccount.DoesNotExist:
#             form.add_error('to_user', 'Recipient account not found.')
#             return self.form_invalid(form)

#     def form_invalid(self, form):
#         return render(self.request, self.template_name, {'form': form})