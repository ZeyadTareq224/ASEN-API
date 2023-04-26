from django.db import models

from asen.common.models import Gender

# Create your models here.
class Patient(models.Model):
    PATIENT_STATUS = [('active', 'Active'), ('disabled', 'Disabled')]
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=PATIENT_STATUS)
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.SET_NULL)
    dob = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"