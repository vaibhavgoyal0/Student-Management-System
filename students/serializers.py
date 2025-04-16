from rest_framework import serializers
from .models import SecondYearStudent, ThirdFourthYearStudent

class SecondYearStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondYearStudent
        fields = ['student_id', 'first_name', 'last_name', 'major', 'email', 'section', 'practicum_details']

class ThirdFourthYearStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdFourthYearStudent
        fields = ['student_id', 'first_name', 'last_name', 'major', 'email', 'section', 'internship_details']