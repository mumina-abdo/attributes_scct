from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from classperiod import ClassPeriod
from .serializers import StudentSerializer
from rest_framework.response import Response

class ClassPeriodListView(APIView):
    def get(self, request ):
        ClassPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
# Create your views here.
