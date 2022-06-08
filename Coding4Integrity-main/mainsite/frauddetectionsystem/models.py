from django.db import models

# Create your models here.

class EnigmaAdmin(models.Model):
    name = models.CharField(max_length =100)
    image = models.ImageField(upload_to = 'pics')
    description = models.TextField()
    class Meta:
        managed = True
        db_table = 'frauddetectionsystem'


class Investigation(models.Model):
    name = models.CharField(max_length =100)
    subject= models.CharField(max_length =100)
    crime = models.CharField(max_length =100)
    action = models.CharField(max_length =100)
    class Meta:
        managed = True
        db_table = 'investigation'



class Mlmodel(models.Model):
    name = models.CharField(max_length =100)
    subject= models.CharField(max_length =100)
    crime = models.CharField(max_length =100)
    action = models.CharField(max_length =100)
    class Meta:
        managed = True
        db_table = 'mlmodel'


class User(models.Model):
    name = models.CharField(max_length =100)
    subject= models.CharField(max_length =100)
    crime = models.CharField(max_length =100)
    action = models.CharField(max_length =100)
    class Meta:
        managed = True
        db_table = 'user'




class USSD(models.Model):
    name = models.CharField(max_length =100)
    subject= models.CharField(max_length =100)
    crime = models.CharField(max_length =100)
    action = models.CharField(max_length =100)
    class Meta:
        managed = True
        db_table = 'ussd'