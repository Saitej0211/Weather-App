from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/get_cities/', views.get_cities, name='get_cities')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)