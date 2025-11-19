# main/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_app.urls')),  # Dashboard, Profile
    path('accounts/', include('allauth.urls')),  # AllAuth routes
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Главная страница

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)