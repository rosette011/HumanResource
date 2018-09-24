from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    numbers = [1,2,3,4,5,6]
    name = 'Rosette Santos'

    context = {'name':name, 'numbers':numbers}
    return render(request, 'human_resource/index.html',context)