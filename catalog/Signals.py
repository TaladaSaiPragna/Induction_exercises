from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Student


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_delete, sender=Student)
def delete_Student(sender, instance=None, *args, **kwargs):
    print("Signal called")


@receiver(post_save, sender=Student)
def save_Student(sender, instance=None, *args, **kwargs):
    print("Post_save Signal called For student model")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
