# -*- coding: utf-8 -*-
#admin admin123
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.core.exceptions import ValidationError
from .models import *
from django.db import transaction

def index(request):
	return render(request, 'login/home.html')
	
def login(request):
	if request.method == 'POST':
		if request.POST['option'] == 'Student':
			try:
				attendance = []
				student = Student.objects.get(email = request.POST['email'], password = request.POST['password'])
				subject = Subject.objects.filter(field = student.field, semester = student.semester)
				for s in subject:
					attendance.append(len(Attendance.objects.filter(rollNo = student.pk, subjectID = s.pk, Attendance = 'P')))
				return render(request, 'login/studentlogin.html', {'student': student, 'lecture_info' : zip(subject, attendance)})
			except Student.DoesNotExist:
				return render(request, 'login/home.html', {'error': 'User Does Not Exist'})
		else:
			try:
				semesters = []
				fields = []
				subjects = []
				teacher = Teacher.objects.get(email = request.POST['email'], password = request.POST['password'])
				for subject in Subject.objects.all():
					semesters.append(subject.semester)
					fields.append(subject.field)
					subjects.append(subject.subject_name)
				return render(request, 'login/select.html', {'semesters' : set(semesters), 'fields' : set(fields), 'subjects' : set(subjects)})
			except Teacher.DoesNotExist:
				return render(request, 'login/home.html', {'error': 'User Does Not Exist'})
	else:
		return HttpResponseForbidden()
		
def attendance(request):
	if request.method == 'POST':
		print(request.POST)
		students = Student.objects.filter(field = request.POST['field'], semester = request.POST['semester'])
		subject = Subject.objects.filter(field = request.POST['field'], semester = request.POST['semester'], subject_name = request.POST['subject'])
		global subjectID
		subjectID = subject[0].pk
		global id
		id = []
		for i in students:
			id.append(i.pk)
		return render(request, 'login/attendance.html', {'students' : students, 'subject' : request.POST['subject'], 'field' : request.POST['field'], 'semester' : request.POST['semester']})
	else:
		return HttpResponseForbidden()
		
def updateAttendance(request):
	if request.method == 'POST':
		presentlist = list(map(int, request.POST.getlist('id[]')))
		print(request.POST.getlist('id[]'))
		absentlist = list(set(id) - set(presentlist))
		print(absentlist)
		for p in presentlist:
			attendance = Attendance.objects.create(rollNo = int(p), subjectID = subjectID, Attendance = 'P')
			attendance.save()
		for a in absentlist:
			attendance = Attendance.objects.create(rollNo = int(a), subjectID = subjectID, Attendance = 'A')
			attendance.save()
		transaction.commit()
		return render(request, 'login/updated.html')
	else:
		return HttpResponseForbidden()