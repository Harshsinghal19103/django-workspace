from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test_ors),
    path('welcome/', views.welcome),
    path('signUp/', views.sign_up),
    path('signIn/', views.sign_in),
]
