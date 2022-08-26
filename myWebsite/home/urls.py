from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('backend', views.backend, name="backend"),
    path('frontend', views.frontend, name="frontend"),
    path('databases', views.databases, name="databases")
]
