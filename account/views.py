from django.shortcuts import render

def login(request):
    return render(request, 'account/login.html')

def home(request):
    return render(request, 'account/index.html')