from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class SlapifyUser(models.Model):
    user_type_choices = [
        ('Admin', 'Admin'),
        ('Artist', 'Artist'),
        ('User', 'User'),
    ]
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    email = models.EmailField(unique=True, default='')
    user_type = models.CharField(max_length=20, choices=user_type_choices, default='User')

def create_user(sender, **kwargs):
    if kwargs['created']:
        slapify_user = SlapifyUser.objects.create(user=kwargs['instance'])
