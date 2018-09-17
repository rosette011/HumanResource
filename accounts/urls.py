from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register, name="register"),
    path('profile/', views.profile_view, name="profile_view"),
    path('profile/edit', views.profile_edit, name="profile_edit"),
    path('profile/change-password', views.change_password, name="change_password"),
    path('reset-password/', auth_views.password_reset , {'template_name':'registration/reset-password.html'},name='password_reset'),
    path('reset-password/done', auth_views.password_reset_done , {'template_name':'registration/reset-password-done.html'},name='password_reset_done'),    
    path('reset/<uidb64>/<token>/', auth_views.reset , {'template_name':'registration/reset-password-done.html'},name='password_reset_done'),    

]