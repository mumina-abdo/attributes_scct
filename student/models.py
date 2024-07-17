from django.db import models
from django.db.models.manager import BaseManager


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length =100)
    code = models.PositiveSmallIntegerField()
    email = models.EmailField()
    country = models.CharField(max_length = 15)
    date_of_birth = models.DateField()
    phone_number=models.CharField(max_length =20, default='default_phone_number')    
    address=models.CharField(max_length =20, default='default_address')
    parent_name=models.CharField(max_length =20,  default='default_parent_name')
    parent_phone_number=models.CharField(max_length =20, default='default_pparent_hone_number')
    
objects : BaseManager ["Student"]
    
    
    
def __str__(self):
       return f"{self.first_name} {self.last_name}"
   