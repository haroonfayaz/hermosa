from django.urls import path
from users.views import UserRegistrationView

urlpatterns = [
    path("",UserRegistrationView.as_view()),

]