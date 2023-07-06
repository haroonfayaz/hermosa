from django import forms
from users.models import User

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'email', 'contact', 'travel_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'travel_date': forms.DateInput(attrs={'class': 'form-control'}),
        }