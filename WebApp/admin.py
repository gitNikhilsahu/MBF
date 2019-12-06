from django.contrib import admin
from WebApp.models import Emp

class EmpAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Salary']
admin.site.register(Emp, EmpAdmin)