from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class Student(models.Model):
    name = models.CharField(max_length=50)
    marks = models.PositiveIntegerField()
    # user = models.ForeignKey(User,on_delete=models.CASCADE)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)