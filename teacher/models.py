from django.db import models


# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length =20)
    last_name = models.CharField(max_length =20)
    nationality = models.CharField(max_length = 20)
    email = models.EmailField()
    teachers_class=models.CharField(max_length = 20)
    teachers_course=models.CharField(max_length = 20)
    teacher_id=models.PositiveBigIntegerField()
    account_number=models.CharField(max_length = 20)
    date_of_joining = models.DateField()
    gender=models.CharField(max_length = 20)
    
    
def __str__(self):
       return f"{self.first_name} {self.last_name}"