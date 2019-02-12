from django.db import models

class Student(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	semester = models.IntegerField()
	field = models.CharField(max_length = 10)
	password = models.CharField(max_length = 16)

class Teacher(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	password = models.CharField(max_length = 16)

class Subject(models.Model):
	subject_name = models.CharField(max_length = 50)
	semester = models.IntegerField()
	field = models.CharField(max_length = 10)
	
class Attendance(models.Model):
	rollNo = models.IntegerField()
	subjectID = models.IntegerField()
	Attendance = models.CharField(max_length = 2)