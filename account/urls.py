from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [

    url(r'^$', views.login, name="login"),

]