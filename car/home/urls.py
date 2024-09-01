from django.urls import path 
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('cars/', views.car, name="car"),
    path('contact/', views.contact, name="contact")
]
