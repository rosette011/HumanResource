from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'accounts'

urlpatterns = [

    path('', views.home, name="home"),
    # path('login', auth_view.login,{'authentication_form': LoginForm}),

]