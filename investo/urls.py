from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
] + static(settings.STATIC_URL , documents_root = settings.STATIC_ROOT)
