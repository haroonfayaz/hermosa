from django import forms
from users.models import TravelBud

class TravelBudForm(forms.ModelForm):

    class Meta:
        model = TravelBud
        fields = '__all__'
       
