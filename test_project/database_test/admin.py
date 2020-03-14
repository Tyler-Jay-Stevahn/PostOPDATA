from django.contrib import admin

# Register your models here.
from .models import database, employees

admin.site.register(database)
admin.site.register(employees)