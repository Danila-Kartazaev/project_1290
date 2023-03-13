from django.db import models

# Create your models here.

#class Lead(models.Model):
#   name = models.CharField(max_length=100)
#    message = models.CharField(max_length=300)

class Base(models.Model):
    min_in = models.IntegerField()
    max_in = models.IntegerField()
    min_out = models.IntegerField()
    max_out = models.IntegerField()
    repeat_n = models.IntegerField()

class TruthTable(models.Model):
    base = models.ForeignKey('Base', related_name='tables')



class RandLevel(models.Model):
    base = models.ForeignKey('Base', related_name='levels')

class NumOperations(models.Model):
    base = models.ForeignKey('Base', related_name='operations')

class Genetic(models.Model):
    base = models.ForeignKey('Base', related_name='genetics')

