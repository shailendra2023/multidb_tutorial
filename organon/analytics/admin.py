from django.contrib import admin
from analytics.models import CustomerMaster, CustomerSourceTimestamp

# Register your models here.
class CustomMasterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerMaster._meta.get_fields()]

admin.site.register(CustomerMaster,CustomMasterAdmin)

class CustomerSourceTimestampAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomerSourceTimestamp._meta.get_fields()]

admin.site.register(CustomerSourceTimestamp,CustomerSourceTimestampAdmin)
