from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def register_user(request):
    return render(request, 'register.html', {})



def home(request):
    # check if logged in

    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
        
    else:
        return render(request, 'home.html', {})


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')

