from django.core.exceptions import ValidationError
from django.db import models
from account.models import UserBankAccount
# Create your models here.
from .constants import TRANSACTION_TYPE
from django.contrib.auth.models import User


class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name = 'transactions', on_delete = models.CASCADE) # ekjon user er multiple transactions hote pare
    amount = models.DecimalField(decimal_places=2, max_digits = 12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    is_bankrupt = models.BooleanField(default=False)
    class Meta:
        ordering = ['timestamp']

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='transaction_account')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)