from django.urls import path
from classperiod import ClassPeriod
urlpatterns = [
    path("classperiod/", ClassPeriodListView.as_view(), name = "classperiod_list_view"),
]