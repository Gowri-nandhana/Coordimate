from django.db import models

# Create your models here.

from django.db import models

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def __str__(self):
        return self.name



class booking_table(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    event=models.CharField(max_length=20)
    event_date=models.DateField()
    guests=models.IntegerField()
    venue=models.CharField(max_length=30)
    message=models.CharField(max_length=50)
    def __str__(self):
        return self.name

