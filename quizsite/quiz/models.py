from __future__ import unicode_literals
from django.db import models

class MCQ(models.Model):
	level = models.PositiveSmallIntegerField()
	question = models.CharField(max_length = 150)
	option1 = models.CharField(max_length = 100)
	option2 = models.CharField(max_length = 100)
	option3 = models.CharField(max_length = 100)
	option4 = models.CharField(max_length = 100)
	answer = models.CharField(max_length = 100)