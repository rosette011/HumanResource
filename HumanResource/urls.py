from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('human_resource/', include('human_resource.urls')),
    path('admin/', admin.site.urls),
]