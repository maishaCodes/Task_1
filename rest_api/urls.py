from django.urls import path
from .views import get_data, Studentlist

urlpatterns = [
    path("get/student-list", Studentlist.as_view()),
]
