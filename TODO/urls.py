
from django.urls import path
from .views import *

urlpatterns = [
    path("add-items/", creat, name="add-items"),
    path("get-all/", get_all, name="get-all"),
    path("home/", home, name="home"), 
    path("about/", about, name="about"),
    path("delete/<int:id>/", delete, name="delete"),
    path("items/<int:id>/", get_data_by_id, name="get_data_by_id"),
    path("update/<int:id>/<str:title>/<str:describtion>/", update, name="update"),

]
