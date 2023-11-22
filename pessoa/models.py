from django.db import models

# Create your models here.
# class Pessoa(models.Models):
#     nome = models.CharField(max_leght=100)
#     idade = models.IntegerField()
class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    idade = models.BigIntegerField()
    raca = models.CharField(max_length=10)
    altura = models. FloatField()