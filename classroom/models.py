from django.db import models
from django.contrib.auth.models import User

from django.db.models.manager import BaseManager

class Classroom(models.Model):
    class_name = models.CharField(max_length =20, default='default_phone_number')  
    class_start_date = models.CharField(max_length =20)
    class_end_date= models.CharField(max_length =20)
    class_capacity= models.PositiveSmallIntegerField()
    class_location = models.CharField(max_length =20)
    class_teacher= models.CharField(max_length =20)
    enrolled_students=models.CharField(max_length =20)
    class_description=models.CharField(max_length =20)
    class_id=models.PositiveSmallIntegerField()
    class_hours=models.PositiveSmallIntegerField()
    
    objects : BaseManager ["Classroom"]

    
    
    def __str__(self):
       return f"{self.class_name} {self.class_start_date}"





# Create your models here.

