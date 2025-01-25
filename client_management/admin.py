from django.contrib import admin
from client_management import models

class companyModalAdmin(admin.ModelAdmin):
    list_display = ['client', 'company_id']

# Register your models here.
admin.site.register(models.NewClientModel)
admin.site.register(models.AddCompanyModel, companyModalAdmin)