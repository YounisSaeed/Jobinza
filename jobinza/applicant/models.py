from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=50, null=False, blank=True)
    address = models.CharField(max_length=50, null=False, blank=True)