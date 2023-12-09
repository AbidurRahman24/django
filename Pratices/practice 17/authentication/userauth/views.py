from django.shortcuts import render, redirect
from .forms import RegisterForm,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def home(request):
    return render(request, './home.html')
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
    else:
        form = RegisterForm()
    return render(request, 'signup.html',{'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            # check kortechi user database e ache kina
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')  # profile page e redirect korbe
            
    else:
        form = AuthenticationForm()
    return render(request, './login.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')
    


def user_logout(request):
    logout(request)
    return redirect('login')