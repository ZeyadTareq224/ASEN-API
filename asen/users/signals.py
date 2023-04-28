from django.dispatch import receiver
from django.db.models.signals import post_save

from asen.patients.models import Patient
from django.contrib.auth import get_user_model


@receiver(post_save, sender=get_user_model())
def create_patient(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)
