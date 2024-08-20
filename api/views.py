from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student
from .serializers import StudentSerializer, MinimalStudentSerializer

from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer, MinimalClassPeriodSerializer

from course.models import Course
from .serializers import CourseSerializer, MinimalCourseSerializer

from classroom.models import Classroom
from .serializers import ClassroomSerializer, MinimalClassroomSerializer

from teacher.models import Teacher
from .serializers import TeacherSerializer, MinimalTeacherSerializer

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        country = request.query_params.get("country")
        if country:
            students = students.filter(country=country)
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassPeriodListView(APIView):
    def get(self, request):
        classperiods = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(classperiods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        class_period = get_object_or_404(ClassPeriod, id=id)
        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data)

    def put(self, request, id):
        class_period = get_object_or_404(ClassPeriod, id=id)
        serializer = ClassPeriodSerializer(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_period = get_object_or_404(ClassPeriod, id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClassroomListView(APIView):
    def get(self, request):
        classrooms = Classroom.objects.all()
        serializer = MinimalClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom = get_object_or_404(Classroom, id=id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)

    def put(self, request, id):
        classroom = get_object_or_404(Classroom, id=id)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classroom = get_object_or_404(Classroom, id=id)
        classroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = MinimalCourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = get_object_or_404(Course, id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)























































































































































































































































































































































































# from django.shortcuts import render

# from rest_framework import status


# from rest_framework.response import Response
# from rest_framework.views import APIView


# from student.models import Student
# from .serializers import StudentSerializer


# from classperiod.models import ClassPeriod
# from .serializers import ClassPeriodSerializer


# from course.models import Course
# from .serializers import CourseSerializer

# from classroom.models import Classroom
# from .serializers import ClassroomSerializer


# from teacher.models import Teacher
# from .serializers import TeacherSerializer


# class StudentListView(APIView):
#     def get(self, request ):
#         students = Student.objects.all()
#         serializer = MinimalStudentSerializer(students, many = True)
#         first_name = request.query_params.get("first_name")
#         if first_name:
#             students = students.filter(first_name=first_name)
#         country = request.query_params.get("country")
#         if country:
#             students = students.filter(country=country)    
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
    
    
#     def post(self, request):
#         serialzer = StudentSerializer(request.data)
#         if serialzer. is_valid():
#             serialzer.save()
#             return Response(serialzer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
# class StudentDetailView(APIView):
#     def get(self, request, id):
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
    
    

    
#     def enroll_student(add, student, course_id):
#         Course = Course.objects.get(id = course_id)
#         student.courses.add(Course)
        
        
#     def post(self, request, id):
#         Student = Student.objects.get(id=id)
#         action = request.data.get("action")
#         if action == "enroll":
#            Course_id =request.data.get("course")
#            self.enroll_student(student = course_id)
             
    
#     def put(self, request, id):
#         student = Student.objects.get(id = id)
#         serializer = StudentSerializer(student, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, id):
#         student = Student.objects.get(id = id)
#         student.delete()
#         return Response(status= status.HTTP_202_ACCEPTED)
    

    
    
   
        
# class ClassPeriodListView(APIView):
#     def get(self, request ):
#         classperiods = ClassPeriod.objects.all()
#         serializer = ClassPeriodSerializer(classperiods, many=True)
#         return Response(serializer.data)
    
    
#     def post(self, request):
#         serialzer = ClassPeriodSerializer(request.data)
#         if serialzer. is_valid():
#             serialzer.save()
#             return Response(serialzer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
# class ClassPeriodDetailView(APIView):
#     def get(self, request, id):
#         ClassPeriod = ClassPeriod.objects.get(id=id)
#         serializer = ClassPeriodSerializer(ClassPeriod)
#         return Response(serializer.data)
    
    
#     def put(self, request, id):
#         ClassPeriod = ClassPeriod.objects.get(id = id)
#         serializer = ClassPeriodSerializer(ClassPeriod, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, id):
#         ClassPeriod = ClassPeriod.objects.get(id = id)
#         ClassPeriod.delete()
#         return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
# class ClassroomListView(APIView):
#     def get(self, request ):
#         classroom = Classroom.objects.all()
#         serializer = ClassroomSerializer(classroom, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serialzer = ClassroomSerializer(request.data)
#         if serialzer. is_valid():
#             serialzer.save()
#             return Response(serialzer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
# class ClassroomDetailView(APIView):
#     def get(self, request, id):
#         Classroom = Classroom.objects.get(id=id)
#         serializer = ClassroomSerializer(Classroom)
#         return Response(serializer.data)
    
    
#     def put(self, request, id):
#         Classroom = Classroom.objects.get(id = id)
#         serializer = StudentSerializer(Classroom, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, id):
#         Classroom = Classroom.objects.get(id = id)
#         Classroom.delete()
#         return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
    
# class CourseListView(APIView):
#     def get(self, request ):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serialzer = CourseSerializer(request.data)
#         if serialzer. is_valid():
#             serialzer.save()
#             return Response(serialzer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
# class CourseDetailView(APIView):
#     def get(self, request, id):
#         Course = Course.objects.get(id=id)
#         serializer = CourseSerializer(Course)
#         return Response(serializer.data)
    
    
#     def put(self, request, id):
#         Course = Course.objects.get(id = id)
#         serializer = CourseSerializer(Course, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, id):
#         Course = Course.objects.get(id = id)
#         Course.delete()
#         return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
# class TeacherListView(APIView):
#     def get(self, request ):
#         teachers = Teacher.objects.all()
#         serializer = TeacherSerializer(teachers, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serialzer = TeacherSerializer(request.data)
#         if serialzer. is_valid():
#             serialzer.save()
#             return Response(serialzer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serialzer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
# class TeacherDetailView(APIView):
#     def get(self, request, id):
#         teacher = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teacher)
#         return Response(serializer.data)
    
    
#     def put(self, request, id):
#         teacher = Teacher.objects.get(id = id)
#         serializer = TeacherSerializer(teacher, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, id):
#         teacher = Teacher.objects.get(id = id)
#         teacher.delete()
#         return Response(status= status.HTTP_202_ACCEPTED)
    
    
    
    
    
   

    