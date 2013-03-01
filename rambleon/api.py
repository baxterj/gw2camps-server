from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from rambleon.models import *
from auth import *
import postHandlers
import getHandlers
from string import *
from decimal import *

sanitizeInput = True


class MyUserAuthorization(Authorization):
	def is_authorized(self, request, object=None):
		return True

	def apply_limits(self, request, object_list):
		if request:
			return object_list.filter(key__iexact=request.GET.get('user'))
		else:
			return object_list.none()


class SessionResource(ModelResource):
	borderlands = fields.ToManyField('rambleon.api.BorderlandResource', 'borderlands', full=True)
	class Meta:
		queryset = Session.objects.all()
		resource_name ='session'
		authentication = Authentication()
		authorization = MyUserAuthorization()
		max_limit=1
		limit=1
		list_allowed_methods = ['get', 'post',]
		always_return_data = True

	def dehydrate(self, bundle):
		return getHandlers.dehydrateSession(bundle=bundle)

	def obj_create(self, bundle, request=None, **kwargs):
		if(sanitizeInput):
			bundle = postHandlers.sanitizeInput(bundle)

		return postHandlers.handleNewSession(bundle)




class BorderlandResource(ModelResource):
	camps = fields.ToManyField('rambleon.api.CampResource', 'camps', full=True)
	class Meta:
		queryset = Borderland.objects.all()
		resource_name ='borderland'
		authentication = Authentication()
		authorization = MyUserAuthorization()
		max_limit=4
		limit=4
		list_allowed_methods = ['get',]
		always_return_data = True

	# def dehydrate(self, bundle):
		# return getHandlers.escapeBundle(getHandlers.dehydrateBorderland(bundle=bundle))

class CampResource(ModelResource):
	class Meta:
		queryset = Camp.objects.all()
		resource_name ='camp'
		authentication = Authentication()
		authorization = MyUserAuthorization()
		max_limit=6
		limit=6
		list_allowed_methods = ['get',]
		always_return_data = True

	def dehydrate(self, bundle):
	 	return getHandlers.dehydrateCamp(bundle=bundle)

class UpdateCampResource(ModelResource):
	class Meta:
		queryset = Camp.objects.all()
		resource_name='updatecamp'
		authentication = Authentication()
		authorization = MyUserAuthorization()
		list_allowed_methods=['post',]
		always_return_data = True

	def obj_create(self, bundle, request=None, **kwargs):
		if(sanitizeInput):
			bundle = postHandlers.sanitizeInput(bundle)
		return postHandlers.handleUpdateCamp(bundle)
