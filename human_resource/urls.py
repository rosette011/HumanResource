from django.urls import path
from . import views

app_name = 'human-resource'

urlpatterns = [

    path('', views.home, name="home"),

]