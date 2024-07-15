from rest_framework import serializers
from course.models import Courses

class CourseSerializer(serializers.ModelSerializer):
    class meta:
        model = Courses
        fields = "--all--"