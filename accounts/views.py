from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    return render(request, 'registration/login.html')

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            auth_login(request,user)
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request,'registration/register.html',context)