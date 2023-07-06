from django.urls import path
from users.views import UserRegistrationView,HomeView

urlpatterns = [
    path("home",HomeView.as_view()),
    path("signup",UserRegistrationView.as_view()),

]