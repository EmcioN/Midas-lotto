from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120, blank=True)
    subscription_expiry = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.user.username
