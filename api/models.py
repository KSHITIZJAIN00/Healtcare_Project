from django.db import models
from django.contrib.auth.models import User

class patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class doctor(models.Model):
    name = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)

class mapping(models.Model):
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
