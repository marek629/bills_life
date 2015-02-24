from django.db import models


class Event(models.Model):
    date = models.DateTimeField('created date')
    url = models.CharField(max_length=1000)
