from django.db import models

# Create your models here.
class Drone(models.Model):
    name =  models.CharField(max_length=30)
    capacity = models.FloatField(default=0)
    battery = models.IntegerField(default =0)
    weight = models.FloatField(default=0)

class Customer(models.Model):
    name =  models.CharField(max_length=30)
    address = models.CharField(max_length=200,default="")
    lat = models.FloatField(default=0)
    long = models.FloatField(default =0)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    priority = models.BooleanField(default=False)