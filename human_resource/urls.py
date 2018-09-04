from django.urls import path
from . import views

app_name = 'human_resource'

urlpatterns = [

    path('', views.home, name="home"),

]