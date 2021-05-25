from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class CoffeeShop(models.Model):
    name = models.CharField(max_length=25)

class CoffeeOption(models.Model):
    name = models.CharField(max_length=25)
    cafienated = models.BooleanField()
    coffeeshop = models.ForeignKey(CoffeeShop,on_delete=models.CASCADE,verbose_name='what shop its in')

class Barrista(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    CoffeeShop = models.ForeignKey(CoffeeShop,on_delete=models.CASCADE,verbose_name='employer')


class CSVFile(models.Model):
    new_file = models.FileField()


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
 

class ProfileInterest(models.Model):
    profile = models.ForeignKey(Profile,on_delete=CASCADE)
    interest = models.CharField(max_length=100)
