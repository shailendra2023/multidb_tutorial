from django.db import models
# Create your models here.

class CustomerMaster(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label="analytics"

class CustomerSourceTimestamp(models.Model):
    custom_master = models.ForeignKey(to=CustomerMaster, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label="analytics"