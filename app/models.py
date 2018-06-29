"""
Definition of models.
"""

from django.db import models
from datetime import date

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=200)
    speciality=models.CharField(max_length=200)

class Patient(models.Model):
    name=models.CharField(max_length=200)
    DOB=models.DateField(default=date.today, blank=True)

class Appointment(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    datetime=models.DateTimeField(blank=True)

class Login(models.Model):
    username=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=200)
    PATIENT='PT'
    DOCTOR='DC'
    SUPERVISOR='SP'
    FRONTDESK='FD'
    TYPE_CHOICES=(
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
        (SUPERVISOR, 'Supervisor'),
        (FRONTDESK, 'FrontDesk'),
    )
    logintype=models.CharField( max_length=2,choices=TYPE_CHOICES,default=PATIENT)




