from django import forms
from users.models import TravelBud

class TravelBudForm(forms.ModelForm):

    class Meta:
        model = TravelBud
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stay_duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'adult': forms.NumberInput(attrs={'class': 'form-control'}),
            'children': forms.NumberInput(attrs={'class': 'form-control'}),
        }
       
