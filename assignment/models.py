from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    # ddmmyyyy
    dob = models.IntegerField(max_length=8, blank=True, null=True)
    parent_name = models.CharField(max_length=25, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    phone = models.IntegerField(max_length=10, blank=True, null=True)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    english = models.IntegerField(default=None)
    maths = models.IntegerField(default=None)
    science = models.IntegerField(default=None)
    hindi = models.IntegerField(default=None)
    social_science = models.IntegerField(default=None)
    percentage = models.FloatField(default=None)