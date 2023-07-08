from users.forms import UserRegistrationForm
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import TravelBudForm
from django.contrib import messages

class HomeView(TemplateView):
    template_name='index.html'

class UserRegistrationView(FormView):
    template_name = 'index.html'
    form_class = TravelBudForm
    success_url = reverse_lazy('registration_success')

    def form_valid(self, form):
        user = form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('home')



