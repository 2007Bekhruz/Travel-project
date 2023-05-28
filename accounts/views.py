from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'pages/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("home")
