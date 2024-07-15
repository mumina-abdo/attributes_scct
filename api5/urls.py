from django.urls import path
from .views import  Classroom

urlpatterns = [
    path("classroom/", ClassroomListView.as_view(), name = "classroom_list_view"),
]