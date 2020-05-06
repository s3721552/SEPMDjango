from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='robot-home'),
    path('tours/', views.tours, name='robot-tours'),
]
