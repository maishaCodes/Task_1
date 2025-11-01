from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics


@api_view(["GET"])
def get_data(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



class Studentlist(APIView):

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("data", request.data)
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)