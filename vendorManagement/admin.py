from django.contrib import admin
from .models import *


class VendorAdmin(admin.ModelAdmin):
    list_display = ['name','contact','details','address','vendor_code']

admin.site.register(Vendor,VendorAdmin)



