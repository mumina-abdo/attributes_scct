from rest_framework import serializers
from teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class meta:
        model = Teacher
        fields = "--all--"