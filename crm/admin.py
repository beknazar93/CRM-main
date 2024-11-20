from django.contrib import admin

from .models import Employee, Client, SalesPipelineStage

# Register your models here.
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(SalesPipelineStage)