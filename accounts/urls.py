from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path('profile/', views.profile_view, name="profile_view"),
    path('profile/edit', views.profile_edit, name="profile_edit"),

]
