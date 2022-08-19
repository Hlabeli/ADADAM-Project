from django.shortcuts import render

'''
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash, login, logout
from django.contrib import messages
'''



'''
- Registration methods to handle both GET and POST Requests


def registration(request):
    if not request.user.is_authenticated:
        if request.method =='GET':
            registration_form = RegistrationForm()
            return render(request, 'users/register.html', {"form": registration_form, 'is_error': False})

        elif request.method == 'POST':
            registration_form = RegistrationForm(data=request.POST)
            if registration_form.is_valid:
                registration_form.save()
                name = registration_form.cleaned_data.get('name')
                messages.success(request, name + '. Account succeffully created! Kindly Login to continue.')

                return redirect(login)

            else:
                return render(request, 'users/registration.html', {"form": registration_form, 'is_error':True})
    else:
        return redirect('adadam-dashboard')

'''

'''
- Login method


def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            login_form = LoginForm()
            return render(request, 'users/login.html', {"form": login_form, 'is_error':False})

        elif request.method == 'POST':
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('profile', user)
                else:
                    return render(request, 'users/login.html', {"form": login_form, 'is_error':True})
            else:
                return render(request, 'user/login.html', )
    else:
        return redirect('adadam-dashboard')

@login_required(login_url='login')
def logout(request):
    messages.success(request, 'Successfully loggout! Kindly login to continues')
    logout(request)
    return redirect('login')

'''