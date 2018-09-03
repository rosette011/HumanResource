from django.shortcuts import render
from django.views.generic import View


def login(request):
    return render(request, 'registration/login.html')