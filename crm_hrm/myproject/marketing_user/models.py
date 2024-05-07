# marketing_user/models.py
from django.db import models
from user_management.models import User  # Import the User model from user_management app

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with User model
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
