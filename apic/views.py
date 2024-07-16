from django.shortcuts import render
from rest_framework.views import APIView
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from rest_framework.response import Response

class ClassPeriodListView(APIView):
    def get(self, request ):
        Classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(Classperiod, many=True)
        return Response(serializer.data)
# Create your views here.