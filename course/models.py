from django.db import models

from student.models import Student

# Create your models here.
class course(models.Model):
    course_name = models.CharField(max_length =20)
    course_id = models.PositiveSmallIntegerField()
    course_description= models.CharField(max_length =20)
    course_credit= models.PositiveSmallIntegerField()
    course_start_date = models.CharField(max_length =20)
    course_end_date= models.CharField(max_length =20)
    course_category=models.CharField(max_length =20)
    course_teacher=models.CharField(max_length =20)
    course_capacity=models.PositiveSmallIntegerField()
    
    
def __str__(self):
       return f"{self.course_name} {self.course_id}"