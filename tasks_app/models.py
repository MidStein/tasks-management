from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    pub_time = models.DateTimeField("time published")

    def __str__(self):
        return self.title
