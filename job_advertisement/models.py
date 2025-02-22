from django.db import models
from client_management.models import AddCompanyModel
from django.contrib.auth.models import User

# Create your models here.
class JobAdvertisementModel(models.Model):
    date_of_app = models.DateField()
    maturity_date = models.DateField()
    expiry_date = models.DateField()
    job_code = models.CharField(max_length=300)
    range_field = models.CharField(max_length=300, null=True)
    no_of_vaccancies = models.IntegerField(null=True)
    designation = models.CharField(max_length=500)
    comp_name = models.ForeignKey(AddCompanyModel, on_delete=models.SET_NULL, null=True)
    date_of_review = models.DateField(null=True)
    no_of_app = models.IntegerField(null=True)
    emp_name = models.CharField(max_length=300, null=True)

class ServerStorageInfoModel(models.Model):
    total_storage = models.IntegerField(null=True)
    user_storage = models.FloatField(null=True)
    total_percent_used = models.FloatField(null=True)

class MyTodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    task = models.TextField(null=True)
    is_completed = models.BooleanField(default=False)

class RealtimeUserActiveModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    active_date = models.DateTimeField()