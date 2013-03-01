from django.http import Http404
from datetime import datetime as dt
from models import *
import geography
import string
from django.utils.html import escape

def dehydrateSession(bundle):
	bundle.data['activeSince'] = bundle.data['activeSince'].strftime('%Y %m %d %H %M %S')
	return bundle

def dehydrateCamp(bundle):
	bundle.data['lastChanged'] = bundle.data['lastChanged'].strftime('%Y %m %d %H %M %S')
	bundle.data['lastUpdate'] = bundle.data['lastUpdate'].strftime('%Y %m %d %H %M %S')
	return bundle

#prevent injection attacks by escaping html elements before return
def escapeBundle(bundle):
	if not isinstance(bundle, Http404):
		return escapeDict(bundle.data)
	return bundle

def escapeDict(inp):
	for key in inp:
		if isinstance(inp[key], basestring):
			inp[key] = escape(inp[key])
		#elif isinstance(inp[key], dict):
			#inp[key] = escapeDict(inp[key])
		elif isinstance(inp[key], list):
			if not key == 'pathpoints':
				newList = []
				for s in inp[key]:
					newList.append(escape(s))
				inp[key] = newList
	return inp

