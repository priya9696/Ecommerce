from django.db import models
from django.contrib import admin

class Category(models.Model):
   Cname=models.CharField(max_length=30,primary_key=True)
   #class Meta:
       #db_table='Category'

class User(models.Model):
    email=models.EmailField(max_length=50,primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=15,unique=True)
    password=models.CharField(max_length=20)

class Product(models.Model):
    Pname=models.CharField(max_length=30)
    Price= models.DecimalField(max_digits=10, decimal_places=2)
    Description=models.TextField(max_length=300)
    Cname=models.ForeignKey(Category,on_delete = models.CASCADE)
   
    class Meta:
        db_table = 'Product'



class feedback(models.Model):
    email=models.ForeignKey(User,on_delete = models.CASCADE)
    Comment=models.TextField(max_length=300)

class Cart(models.Model):
    pid=models.ForeignKey(Product,null=True, on_delete =models.CASCADE)
    email=models.ForeignKey(User, on_delete = models.CASCADE)
    qty=models.IntegerField(default=1)

class MyOrders(models.Model):
    qty=models.ForeignKey(Cart,on_delete = models.CASCADE)
    Price= models.ForeignKey(Product,on_delete = models.CASCADE)
    subt= models.IntegerField()
    
    def __str__(self):
        return self.subt
    





    
    

