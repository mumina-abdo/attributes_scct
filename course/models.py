from django.db import models
from django.db.models.manager import BaseManager




# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length =20)
    course_id = models.PositiveSmallIntegerField()
    course_description= models.CharField(max_length =20)
    course_credit= models.PositiveSmallIntegerField()
    course_start_date = models.CharField(max_length =20)
    course_end_date= models.CharField(max_length =20)
    course_category=models.CharField(max_length =20)
    course_teacher=models.CharField(max_length =20)
    course_capacity=models.PositiveSmallIntegerField()
    
objects : BaseManager ["Course"]
    
    
def __str__(self):
       return f"{self.course_name} {self.course_id}"