from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from shoppingapp.forms import LoginRegister, UserRegister


# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_shopkeeper:
                return redirect('shopkeeper_home')
            elif user.is_user:
                return redirect('user_home')
        else:
            messages.info(request, 'INVALID CREDENTIALS')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def user_registery(request):
    login_form = LoginRegister()
    user_form = UserRegister()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegister(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            c = user_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, 'User Registered Successfully')
            return redirect('login')
    return render(request, 'user_register.html', {'login_form': login_form, 'user_form': user_form})
