from rest_framework import serializers
from .models import SecondYearStudent, ThirdFourthYearStudent

class SecondYearStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondYearStudent
        fields = '__all__'

class ThirdFourthYearStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdFourthYearStudent
        fields = '__all__'