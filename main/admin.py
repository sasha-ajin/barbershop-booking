from django.contrib import admin
from . models import Barber,Order,Time

admin.site.register(Barber)
admin.site.register(Order)
admin.site.register(Time)