from .views import RegistrationView
from django.urls import path

urlspatterns = [
    path('register', RegistrationView.as_view(), name="register")
]