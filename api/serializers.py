from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from course.models import Course
from classroom.models import Classroom
from teacher.models import Teacher


class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']

class StudentSerializer(MinimalStudentSerializer):
    class Meta(MinimalStudentSerializer.Meta):
        fields = '__all__'  

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ['id', 'name'] 

class ClassPeriodSerializer(MinimalClassPeriodSerializer):
    class Meta(MinimalClassPeriodSerializer.Meta):
        fields = '__all__'  

class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']  

class CourseSerializer(MinimalCourseSerializer):
    class Meta(MinimalCourseSerializer.Meta):
        fields = '__all__'  

class MinimalClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name']  

class ClassroomSerializer(MinimalClassroomSerializer):
    class Meta(MinimalClassroomSerializer.Meta):
        fields = '__all__'  

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']  

class TeacherSerializer(MinimalTeacherSerializer):
    class Meta(MinimalTeacherSerializer.Meta):
        fields = '__all__'  















































































































































































# from rest_framework import serializers
# from student.models import Student
# from classperiod.models import ClassPeriod
# from course.models import Course
# from teacher.models import Teacher
# from classroom.models import Classroom





# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields="__all__"
        
# class ClassPeriodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ClassPeriod
#         fields="__all__"     
        
        
        
           
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Course
#         fields="__all__"     
               

    
        
# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Teacher
#         fields="__all__"     
             
        
# class ClassroomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Classroom
#         fields="__all__"     
        
        
        
# class MinimalStudentSerializer (serializers.ModelSerializer):
    
#     class meta:
#         model = Student
#         fields = ["first_name","email"]     