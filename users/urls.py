from django.urls import path
from users.views import UserRegistrationView

urlpatterns = [
    path("signup",UserRegistrationView.as_view()),
]