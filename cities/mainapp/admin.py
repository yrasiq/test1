from django.contrib import admin
from .models import Citizen, City


admin.site.register(City)
admin.site.register(Citizen)
