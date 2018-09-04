from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.login_redirect, name='login_redirect'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('human_resource/', include('human_resource.urls')),
    path('admin/', admin.site.urls),
]