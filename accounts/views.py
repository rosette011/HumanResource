from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import View


def login(request):
    return render(request, 'accounts/login.html')


def home(request):
    return render(request, 'accounts/index.html')