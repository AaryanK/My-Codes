from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="dashboard/7.png")




class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    RATINGS = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    available_number = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    ratings = models.IntegerField(default=0,choices=RATINGS)

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
            


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)



class Cart(models.Model):
    products = models.ManyToManyField(CartItem)
    

class Order(models.Model):
    choices = (
        ('pending','pending'),
        ('cancelled','cancelled'),
        ('delivered','delivered')
    )
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    order_number = models.IntegerField(blank=True,null=True)
    status = models.CharField(choices=choices,default="pending",max_length=20)
    place = models.CharField(max_length=200,blank=True)
    phone_number = models.IntegerField(blank=True,null=True)

    	
    
