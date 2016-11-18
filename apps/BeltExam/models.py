from __future__ import unicode_literals
from django.db import models
from ..LoginAndReg.models import User, LoginManager, RegisterManager

class Trip(models.Model):
	destination = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	creater = models.ForeignKey(User)
	fromDate = models.DateField()
	toDate = models.DateField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class Trip_Users(models.Model):
	trip = models.ForeignKey(Trip, related_name = "trip_users")
	User = models.ForeignKey(User, related_name = "user_trips")


