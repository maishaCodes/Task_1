
from django.urls import path
from.views import index,about,update
urlpatterns = [
    path("index/", index, name="index"),
    path("about/", about, name="about"),
    path("update/", about, name="update"),
]
