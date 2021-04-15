from django.db import models

# Create your models here.
class ItemA(models.Model):
    comapany_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.IntegerField()

class ItemB(models.Model):
    comapany_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.IntegerField()

class ItemC(models.Model):
    comapany_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.IntegerField()
