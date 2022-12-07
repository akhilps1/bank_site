from django.contrib import messages, auth
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect

# # Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('user created')
                return redirect('credentials:login')
        else:
            messages.info(request, 'password not matching')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            current_user = request.user
            return redirect('details:detail')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('credentials:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('main:home')