from django.db import models

# Create your models here.
class database(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=25)
    description = models.TextField()

class employees(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=25)
    description = models.TextField()
