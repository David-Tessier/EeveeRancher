from django.contrib import admin
from .models import Pet

# Register your models here.

class PetAdmin(admin.ModelAdmin):
    fields=['name','owner','birth_date','age']

admin.site.register(Pet)
