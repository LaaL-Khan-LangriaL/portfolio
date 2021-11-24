from django.db import models

# Create your models here.


class add_Review(models.Model):
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    comment = models.TextField(default="")