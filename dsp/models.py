from django.db import models

# Create your models here.
from taggit.managers import TaggableManager

class Project(models.Model):
    # ... fields here
    tags = TaggableManager()

class PTFormInput(models.Model):
	day_of_week = models.CharField(max_length=10)
	week_of_month = models.CharField(max_length=10)
	def __str__(self):
		return self.day_of_week, self.week_of_month