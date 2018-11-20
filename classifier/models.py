from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AllowedToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=30)

class Class(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)

class Feedback(models.Model):
    fclass = models.OneToOneField(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
