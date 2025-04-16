from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    send = models.TextField()
    recive = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)