from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=34)
    dob = models.DateField()
    gender = models.CharField(max_length=23)
    marks = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profile')