from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('', views.index, name='index')
]
