from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AllowedToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=30)
