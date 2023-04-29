from django.db import models
from django.utils.timezone import now


# Create your models here.
class Response(models.Model):
    prompt = models.CharField()
    response = models.CharField()
    publication_date = models.DateTimeField(default=now())
