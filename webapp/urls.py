from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('', views.index, name='index')
]

if settings.DEBUG :
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
