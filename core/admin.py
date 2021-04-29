from django.contrib import admin

from core.models import Prisoner

class PrisonerAdmin(admin.ModelAdmin):
	fields = (
		'name',
		'matriculation'
	)

admin.site.register(Prisoner, PrisonerAdmin)
