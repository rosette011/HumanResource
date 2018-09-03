from django.shortcuts import render, redirect
from django.views.generic import View

def home(request):
    return render(request, 'human_resource/index.html')