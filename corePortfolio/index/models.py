from django.db import models

# Create your models here.


class hello(models.Model):
    yourName = models.CharField(max_length=100, default="")
    yourSubject = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=100, default="")