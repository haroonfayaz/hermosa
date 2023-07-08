from rest_framework import serializers
from .models import User,TravelBud

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'contact', 'travel_date']

class TravelBudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelBud
        fields ='__all__'