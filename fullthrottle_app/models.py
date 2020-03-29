from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from fullthrottle_project import settings

# ActivityPeriod Model
class ActivityPeriod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time =  models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

# Customizing User Model
class User(AbstractUser):
    TIME_ZONE = (
        ('America/Los_Angeles', 'America/Los_Angeles'),
        ('Asia/Kolkata', 'Asia/Kolkata'),     
    )
    tz = models.CharField(max_length=100,
        choices=TIME_ZONE,
        
    )
