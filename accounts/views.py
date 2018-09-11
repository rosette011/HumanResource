from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('human_resource:home')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('human_resource:home')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile_view(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html',args)


def profile_edit(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile_edit.html',args)
