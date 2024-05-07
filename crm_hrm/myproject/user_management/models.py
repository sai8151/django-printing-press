# user_management/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [('marketing', 'Marketing'), ('client', 'Client')]
    role = models.CharField(max_length=10, choices=role_choices)

    def __str__(self):
        return self.user.username
