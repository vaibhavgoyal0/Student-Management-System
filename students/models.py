from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"