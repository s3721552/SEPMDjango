from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
	description = models.TextField()
	x_coordinate = models.DecimalField(max_digits=19, decimal_places=10)
	y_coordinate = models.DecimalField(max_digits=19, decimal_places=10)
	min_timespent = models.IntegerField()
	location = models.CharField(max_length=100)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.description