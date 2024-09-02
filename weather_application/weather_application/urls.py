from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/get_cities/', views.get_cities, name='get_cities')
]