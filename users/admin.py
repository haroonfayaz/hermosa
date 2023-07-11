from django.contrib import admin
from users.models import TravelBud,Destination


class TravelBudAdmin(admin.ModelAdmin):
    list_display = ("name","contact","city","adult","children")


class DestinaionAdmin(admin.ModelAdmin):
    list_display =  ("name","description","image_url")

admin.site.register(TravelBud,TravelBudAdmin)
admin.site.register(Destination,DestinaionAdmin)