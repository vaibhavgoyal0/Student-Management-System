from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import SecondYearStudent, ThirdFourthYearStudent
from .serializers import SecondYearStudentSerializer, ThirdFourthYearStudentSerializer

class SecondYearStudentListCreateView(generics.ListCreateAPIView):
    queryset = SecondYearStudent.objects.all()
    serializer_class = SecondYearStudentSerializer

class ThirdFourthYearStudentListCreateView(generics.ListCreateAPIView):
    queryset = ThirdFourthYearStudent.objects.all()
    serializer_class = ThirdFourthYearStudentSerializer