from django.db import models

# Create your models here.
class CutomUser(models.Model):
    userid = models.CharField(max_length=9, primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Product(models.Model):
    productid = models.CharField(max_length=11, primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    porduct_price = models.DecimalField(max_digits=1000, decimal_places=2)

class UserProfile(models.Model):
    userid = models.OneToOneField(CutomUser,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Subscription(models.Model):
    userid = models.ForeignKey(CutomUser,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_data = models.DateField()



