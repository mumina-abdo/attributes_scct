from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView


from student.models import Student
from .serializers import StudentSerializer


from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer


from course.models import Course
from .serializers import CourseSerializer

from classroom.models import Classroom
from .serializers import ClassroomSerializer


from teacher.models import Teacher
from .serializers import TeacherSerializer


class StudentListView(APIView):
    def get(self, request ):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)



class ClassPeriodListView(APIView):
    def get(self, request ):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)
    
    
class ClassroomListView(APIView):
    def get(self, request ):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    
    
    
class CourseListView(APIView):
    def get(self, request ):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    
class TeacherListView(APIView):
    def get(self, request ):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)