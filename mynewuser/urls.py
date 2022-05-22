from . import views
from django.urls import path

urlpatterns = [
    path('', views.auth, name = 'auth'),
    path('register/', views.register, name='register')
]
