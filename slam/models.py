from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Slam_session(models.Model):
	slam_name = models.CharField(max_length=200)
	number_of_rounds = models.IntegerField()
	number_of_judges = models.IntegerField()
	poet_1 = models.CharField(max_length=200)
	poet_2 = models.CharField(max_length=200)
	poet_3 =models.CharField(max_length=200)
	def __str__(self):
		return self.slam_name

class Judges_scores(models.Model):
	score_1 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_2 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_3 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_4 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	score_5 = models.FloatField(max_length=50, validators = [MinValueValidator(0.0), MaxValueValidator(10.0)])
	
	
class Poet(models.Model):
	round_1 = models.ForeignKey(Judges_scores, related_name='round_1')
	round_2 = models.ForeignKey(Judges_scores, related_name='round_2')
	round_3 = models.ForeignKey(Judges_scores, related_name='round_3')

	
	
