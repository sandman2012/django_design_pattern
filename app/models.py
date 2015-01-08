from django.db import models
import datetime

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ('created',)
