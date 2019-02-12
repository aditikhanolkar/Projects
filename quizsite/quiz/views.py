from __future__ import unicode_literals
from django.shortcuts import render
from .models import MCQ
import random
from django.http import Http404, HttpResponse, HttpResponseForbidden, HttpResponseBadRequest

def index(request):
	return render(request, 'quiz/home.html')
	
def level(request, num):
	try:
		mcqs = []
		mcq = MCQ.objects.filter(level=num)
		ids = random.sample(range(20), 10)

		for id in ids:
			mcqs.append(mcq[id])
		return render(request, "quiz/quiz.html", {'mcqs' : mcqs})
	except Exception as e:
		print(e)
		raise Http404()

def score(request):
	try:
		return render(request, 'quiz/score.html', {'score': request.GET['score']})
	except:
		return HttpResponseForbidden()