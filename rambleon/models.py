from django.db import models
from django.utils import timezone
import datetime


class Session(models.Model):
	key = models.CharField(max_length=60)
	activeSince = models.DateTimeField(auto_now_add=True)

class Borderland(models.Model):
	session = models.ForeignKey(Session, related_name='borderlands')
	name = models.CharField(max_length=5)#red, green, blue, eb
	server = models.CharField(max_length=60)

class Camp(models.Model):
	borderland = models.ForeignKey(Borderland, related_name='camps')
	name = models.CharField(max_length=60)
	color = models.CharField(max_length=5)#red, green, blue, grey
	lastChanged = models.DateTimeField()
	lastUpdate = models.DateTimeField()