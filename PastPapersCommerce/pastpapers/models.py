from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


# Create your models here.




class College(models.Model):
    name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True,blank=True)

class Learner(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name