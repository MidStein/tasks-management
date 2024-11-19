from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
