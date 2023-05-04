from django.dispatch import receiver
from django.db.models.signals import post_save

from asen.patients.models import Patient
from django.contrib.auth import get_user_model
from .tasks import send_welcome_email


User = get_user_model()


@receiver(post_save, sender=User)
def create_patient_on_user_creation(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)


@receiver(post_save, sender=User)
def send_welcome_email_on_user_creation(sender, instance, created, **kwargs):
    if created:
        send_welcome_email.delay(instance.email)
