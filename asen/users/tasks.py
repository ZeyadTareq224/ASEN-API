from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(user_email):
    subject = "Welcome to our site!"
    message = "Thank you for registering on our site."
    from_email = "ziyadtr101@gmail.com"
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
    return "done"
