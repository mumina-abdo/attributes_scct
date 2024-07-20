from django.shortcuts import render

from rest_framework import status


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
    
    
    def post(self, request):
        serialzer = StudentSerializer(request.data)
        if serialzer. is_valid():
            serialzer.save()
            return Response(serialzer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    
    def put(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    

    
    
   
        
class ClassPeriodListView(APIView):
    def get(self, request ):
        classperiods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serialzer = ClassPeriodSerializer(request.data)
        if serialzer. is_valid():
            serialzer.save()
            return Response(serialzer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        ClassPeriod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(ClassPeriod)
        return Response(serializer.data)
    
    
    def put(self, request, id):
        ClassPeriod = ClassPeriod.objects.get(id = id)
        serializer = ClassPeriodSerializer(ClassPeriod, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, id):
        ClassPeriod = ClassPeriod.objects.get(id = id)
        ClassPeriod.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
class ClassroomListView(APIView):
    def get(self, request ):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serialzer = ClassroomSerializer(request.data)
        if serialzer. is_valid():
            serialzer.save()
            return Response(serialzer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class ClassroomDetailView(APIView):
    def get(self, request, id):
        Classroom = Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(Classroom)
        return Response(serializer.data)
    
    
    def put(self, request, id):
        Classroom = Classroom.objects.get(id = id)
        serializer = StudentSerializer(Classroom, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, id):
        Classroom = Classroom.objects.get(id = id)
        Classroom.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
    
class CourseListView(APIView):
    def get(self, request ):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serialzer = CourseSerializer(request.data)
        if serialzer. is_valid():
            serialzer.save()
            return Response(serialzer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class CourseDetailView(APIView):
    def get(self, request, id):
        Course = Course.objects.get(id=id)
        serializer = CourseSerializer(Course)
        return Response(serializer.data)
    
    
    def put(self, request, id):
        Course = Course.objects.get(id = id)
        serializer = CourseSerializer(Course, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, id):
        Course = Course.objects.get(id = id)
        Course.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
class TeacherListView(APIView):
    def get(self, request ):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serialzer = TeacherSerializer(request.data)
        if serialzer. is_valid():
            serialzer.save()
            return Response(serialzer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    
    def put(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
    
    
   

    