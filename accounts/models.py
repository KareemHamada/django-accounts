from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,null=True,blank=True)
    address = models.CharField(max_length=50,blank=True,null=True)
    # image
    # age
    #job

    def __str__(self):
        return str(self.user)
