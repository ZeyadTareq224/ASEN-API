from django.db import models

# Create your models here.
class Gender(models.Model):
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.type