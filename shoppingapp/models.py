from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_shopkeeper = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class shopkeeper(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='shop')
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    address = models.TextField()
    phone_no = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.company_name


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    address = models.TextField()
    phone_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    shop = models.ForeignKey(shopkeeper, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='appiontment')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='schedule')
    status = models.IntegerField(default=0)
