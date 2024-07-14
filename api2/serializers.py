from rest_framework import serializers
from classperiod.models import ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
    class meta:
        model = ClassPeriod
        fields = "--all--"