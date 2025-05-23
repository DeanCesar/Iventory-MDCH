from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    image = models.ImageField(default='avatar.jpg',upload_to='Profile_Images/')

    def __str__(self):
        return f'{self.customer.username}-Profile'

# Create your models here.
