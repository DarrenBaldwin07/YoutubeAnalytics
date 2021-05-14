from django.db import models

# Create your models here.

class User_data(models.Model):
    stats = models.TextField(null=True)