from django.db import models

class SecondYearStudent(models.Model):
    student_id = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    section = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], blank=True, null=True)
    practicum_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Second Year)"

class ThirdFourthYearStudent(models.Model):
    student_id = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    section = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], blank=True, null=True)
    internship_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (3rd/4th Year)"