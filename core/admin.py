from django.contrib import admin

from core.models import Prisoner

class PrisonerAdmin(admin.ModelAdmin):
	exclude = ['created_at', 'updated_at']
	list_display = (
		'name',
		'matriculation',
		'included',
		'excluded',
	)

admin.site.register(Prisoner, PrisonerAdmin)
