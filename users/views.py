from django.shortcuts import redirect ,render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import TravelBudForm
from users.models import Destination
import pyrebase
import json


config ={
   "apiKey": "AIzaSyCS1kgmQ1bGqo9lDDQ_kYP9cT0-TRQvZBY",
    "authDomain": "hermosatravels-fb4d5.firebaseapp.com",
    "databaseURL": "https://hermosatravels-fb4d5-default-rtdb.firebaseio.com/",
    "projectId": "hermosatravels-fb4d5",
    "storageBucket": "hermosatravels-fb4d5.appspot.com",
    "messagingSenderId": "155763168260",
    "appId": "1:155763168260:web:5301d22852e575de81d151",
    "measurementId": "G-ZHTCPML50P"
  }

firebase = pyrebase.initialize_app(config)


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dests"] = Destination.objects.all()
        return context


class UserRegistrationView(FormView):
    template_name = 'index.html'
    form_class = TravelBudForm
    success_url = reverse_lazy('registration_success')

    def form_valid(self, form):
        database = firebase.database()
        
        new_key = database.generate_key()
        
        data = form.cleaned_data
        data['travel_date'] = data['travel_date'].strftime('%Y-%m-%d')
        print(data)
        
        database.child('users').child(new_key).set(data)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('home')
    
class AboutView(TemplateView):
    template_name="about.html"
