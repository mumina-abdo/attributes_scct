from django.db import models
from course.models import Course
# Create your models here.

class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=10)
    classroom = models.CharField(max_length=10)
    day_of_week = models.CharField(max_length=10)
    
    def __str__(self):
        return self.classroom
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


