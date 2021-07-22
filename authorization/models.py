

from django.db import models


# Create your models here.
from django.utils import timezone


class EmailAuth(models.Model):
    username = models.CharField(max_length=120, null=True, blank=False)
    email = models.EmailField(max_length=120, null=True, blank=False)
    num = models.IntegerField(null=True, blank=False)
    created_time = models.TimeField(auto_created=True,null=False,default=timezone.now)

    def __str__(self):
        return self.email
