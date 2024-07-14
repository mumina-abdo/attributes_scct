from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length =20)
    last_name = models.CharField(max_length =20)
    code = models.PositiveSmallIntegerField()
    email = models.EmailField()
    country = models.CharField(max_length = 20)
    date_of_birth = models.DateField()
    phone_number=models.CharField(max_length =20)
    Address=models.CharField(max_length =20)
    parent_name=models.CharField(max_length =20)
    parent_phone_number=models.CharField(max_length =20)
    
    
    
def __str__(self):
       return f"{self.first_name} {self.last_name}"
   