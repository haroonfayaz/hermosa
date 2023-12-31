from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator



class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField(null=True)
    travel_date= models.DateField(null=True)


class TravelBud(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    contact = models.CharField(max_length=15, validators=[MinLengthValidator(10)])
    travel_date = models.DateField()
    city = models.CharField(max_length=100)
    adult = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    children = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    
    class Meta:
        db_table = 'Travelers'

class Destination(models.Model):
    name= models.CharField(max_length=255)
    description =models.CharField(max_length=3555)
    image_url =models.CharField(max_length=2083)

    class Meta:
        db_table ="Destination"


 