
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
# Create your models here.
from django.utils import timezone

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4)


class EmailAuth(models.Model):
    username = models.CharField(max_length=120, null=True, blank=False)
    email = models.EmailField(max_length=120, null=True, blank=False)
    num = models.IntegerField(null=True, blank=False)
    created_time = models.TimeField(auto_created=True,null=False,default=timezone.now)
    

    def __str__(self):
        return self.email
