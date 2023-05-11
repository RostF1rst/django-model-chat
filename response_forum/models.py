from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.
class Response(models.Model):
    prompt = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000)
    publication_date = models.DateTimeField(default=now())
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Response #{}: {}".format(self.id, self.prompt)
