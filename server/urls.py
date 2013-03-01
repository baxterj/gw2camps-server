from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#enable tastypie for RESTful interaction
from tastypie.api import Api
from rambleon.api import *

v1_api = Api(api_name='v1')
v1_api.register(SessionResource())
v1_api.register(BorderlandResource())
v1_api.register(CampResource())
v1_api.register(UpdateCampResource())



#handler500 = 'rambleon.views.custom500view'

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'server.views.home', name='home'),
	# url(r'^server/', include('server.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'rambleon.views.index'),
	url(r'^route/(?P<route_id>\d+)/$', 'rambleon.views.route'),
	url(r'^api/', include(v1_api.urls)),
	# url(r'^login/', 'rambleon.views.login'),
	# url(r'^register/', 'rambleon.views.register'),
	url(r'^test/', 'rambleon.views.test'),
	
)
