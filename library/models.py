import datetime

from django.db import models

class Author(models.Model):
    name: str = models.CharField(max_length=100)
    surname: str  = models.CharField(max_length=100)
    date_for_birth: datetime.datetime  = models.DateTimeField()
