from django.urls import path
from .views import  Class
from django.urls import path


urlpatterns = [
    path("students/", StudentListView.as_view(), name = "student_list_view"),
]