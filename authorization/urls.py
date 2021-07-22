from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('register', views.register_page),
    path('register/activate', views.activate),
    path('login', views.login_page),
    path('logout', views.log_out),
]
