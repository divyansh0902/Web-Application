'''defines URL patterns for users'''
from django.urls import path, include
from . import views

app_name = 'users' #so django can distinguish between urls of other apps
urlpatterns = [
    #include default auth urls
    path('', include('django.contrib.auth.urls')),
    #registration page
    path('register/', views.register, name='register'),
]