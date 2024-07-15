from rest_framework import serializers
from Class.models import Classroom

class TeacherSerializer(serializers.ModelSerializer):
    class meta:
        model = Classroom
        fields = "--all--"
