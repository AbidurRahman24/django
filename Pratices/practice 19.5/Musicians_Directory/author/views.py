from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = forms.RegistertionForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_login')
    else:
        signup_form = forms.RegistertionForm()
    return render(request, 'signup.html', {'form' : signup_form, 'type' : 'Sign Up'})

# Register class base 
class SignupView(CreateView):
    form_class = forms.RegistertionForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('homepage')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('homepage')
    else:
        form = AuthenticationForm()
        return render(request, 'signup.html', {'form' : form, 'type' : 'Login'})

class UserLoginView(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def user_logout(request):
    logout(request)
    return redirect('user_login')


