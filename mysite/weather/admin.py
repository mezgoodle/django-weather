from django.contrib import admin
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('id',)
    search_fields = ['name',]
