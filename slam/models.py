from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Slam_session(models.Model):
	slam_name = models.CharField(max_length=200)
	number_of_rounds = models.IntegerField()
	number_of_judges = models.IntegerField()
	poet = models.CharField(max_length=200)
	
	def __str__(self):
		return self.slam_name


class Poet(models.Model):
	poet_name = models.CharField(max_length=200)
#	slam_details = models.ForeignKey('Slam_session', null=True, blank=True)
	
	def __str__(self):
		return self.poet_name


class Judges_scores(models.Model):
	score_1 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_2 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_3 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_4 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_5 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	
	

	
	
