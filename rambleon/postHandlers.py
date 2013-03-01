from django.http import Http404
from datetime import datetime as dt
from models import *
import string
from decimal import *
import auth
from django.core.mail import send_mail
import getHandlers
import info
from django.utils.timezone import utc

#Methods here should take a tastypie bundle
#they should return the modified bundle or 
#raise a Http404('error description')

def sanitizeInput(bundle):
	bundle.data = getHandlers.escapeDict(bundle.data)
	return bundle


def handleNewSession(bundle):
	key = bundle.data.get('key')

	if Session.objects.filter(key__iexact=key).count() != 0:
		raise Http404('Session name aleady in use')

	try:
		newSession = Session.objects.create(key=key, activeSince=getNow())

		redBorder = Borderland.objects.create(session=newSession, name='red', server=bundle.data.get('red'))
		#camps for red borderland
		for i in range(6):
			Camp.objects.create(borderland=redBorder, name=info.redCamps[i], color='grey', lastChanged=getNow(), lastUpdate=getNow())

		blueBorder = Borderland.objects.create(session=newSession, name='blue', server=bundle.data.get('blue'))
		#camps for blue borderland
		for i in range(6):
			Camp.objects.create(borderland=blueBorder, name=info.blueCamps[i], color='grey', lastChanged=getNow(), lastUpdate=getNow())

		greenBorder = Borderland.objects.create(session=newSession, name='green', server=bundle.data.get('green'))
		#camps for green borderland
		for i in range(6):
			Camp.objects.create(borderland=greenBorder, name=info.greenCamps[i], color='grey', lastChanged=getNow(), lastUpdate=getNow())

		eb = Borderland.objects.create(session=newSession, name='eb', server='Eternal Battlegrounds')
		#camps for eternal battlegrounds
		for i in range(6):
			Camp.objects.create(borderland=eb, name=info.ebCamps[i], color='grey', lastChanged=getNow(), lastUpdate=getNow())

		bundle.obj = newSession
	except Exception:
		raise Http404('An error occurred when creating the session')

	return bundle



def getNow():
	return dt.utcnow().replace(tzinfo=utc)

def handleUpdateCamp(bundle):
	campID = bundle.data.get('id')
	color = bundle.data.get('color')

	try:
		camp = Camp.objects.get(pk=campID)
	except Exception:
		raise Http404('Camp not found')

	if bundle.request.GET.get('user').lower() != camp.borderland.session.key.lower():
		raise Http404 ('Invalid Session code')

	if camp.color != color:
		camp.color = color
		camp.lastChanged = getNow()
	
	camp.lastUpdate = getNow()
	camp.save()
	
	bundle.obj = camp
	return bundle