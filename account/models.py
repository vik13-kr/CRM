from django.db import models
from django.urls import reverse # to use reverse method
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null= True, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100,null =True)
    phone = models.CharField(max_length = 12,null =True)
    email = models.CharField(max_length = 32,null =True)
    profile_pic = models.ImageField(default= "profile.png", null = True, blank = True)
    date_created = models.DateField(auto_now_add = True,null =True)

    def get_absolute_url(self):
        return reverse("customer", kwargs={"pk": self.pk})
    

    def __str__(self):
        if self.name == None:
            return 'No name'
        else:
            return self.name


class Product(models.Model):

    name = models.CharField(max_length = 64,null =True)
    Price = models.FloatField(null = True)
    category = models.CharField(max_length = 100,null =True)
    description = models.TextField(null =True)
    date_created = models.DateField(auto_now_add = True,null =True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, on_delete= models.CASCADE )
    product = models.ForeignKey(Product, on_delete = models.CASCADE )
    date_ordered = models.DateField(auto_now_add = True, null =True)
    status = models.CharField( max_length=50, null = True, choices = STATUS)

    



  


