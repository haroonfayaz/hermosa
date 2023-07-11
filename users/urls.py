from django.urls import path
from users.views import UserRegistrationView,HomeView,AboutView

urlpatterns = [
    path("home",HomeView.as_view(),name='home'),
    path("signup",UserRegistrationView.as_view(),name='signup'),
    path("about",AboutView.as_view(),name='about'),


]