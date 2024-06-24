from django.db import models

from student.models import Student


# Create your models here.

class Classroom(models.Model):
    class_name = models.CharField(max_length =20)
    class_start_date = models.CharField(max_length =20)
    class_end_date= models.CharField(max_length =20)
    class_capacity= models.PositiveSmallIntegerField()
    class_location = models.CharField(max_length =20)
    class_teacher= models.CharField(max_length =20)
    enrolled_students=models.CharField(max_length =20)
    class_description=models.CharField(max_length =20)
    class_id=models.PositiveSmallIntegerField()
    class_hours=models.PositiveSmallIntegerField()
    
    
def __str__(self):
       return f"{self.class_name} {self.class_start_date}"
