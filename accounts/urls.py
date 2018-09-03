from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('login', views.index, name="login"),
    path('register', views.register, name="register"),

]