from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [

    url(r'^$', views.home, name="home"),
    url(r'^account/login$', views.login, name="login"),

]