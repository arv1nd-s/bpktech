from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    # ddmmyyyy
    dob = models.IntegerField(max_length=8)
    parent_name = models.CharField(max_length=25)
    address = models.TextField()
    city = models.CharField(max_length=25)
    phone = models.IntegerField(max_length=10)

class Marks(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    english = models.IntegerField(max_length=2, default=None)
    maths = models.IntegerField(max_length=2, default=None)
    science = models.IntegerField(max_length=2, default=None)
    hindi = models.IntegerField(max_length=2, default=None)
    social_science = models.IntegerField(max_length=2, default=None)