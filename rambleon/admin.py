from rambleon.models import *
from django.contrib import admin

class BorderlandInline(admin.TabularInline):
	model = Borderland
	extra = 0

class SessionAdmin(admin.ModelAdmin):
	list_display=('key', 'activeSince')
	inlines=[BorderlandInline]

admin.site.register(Session, SessionAdmin)

class CampInline(admin.TabularInline):
	model = Camp
	extra = 0

class BorderlandAdmin(admin.ModelAdmin):
	list_display=('session', 'name', 'server')
	inlines=[CampInline]

admin.site.register(Borderland, BorderlandAdmin)

class CampAdmin(admin.ModelAdmin):
	list_display=('borderland', 'name', 'color', 'lastChanged', 'lastUpdate')

admin.site.register(Camp, CampAdmin)