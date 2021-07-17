import datetime

from django.db import models


class Prisoner(models.Model):
	name = models.CharField(
		verbose_name='Nome',
		max_length=30
	)
	matriculation = models.CharField(
		verbose_name='Matrícula',
		max_length=9
	)
	included = models.DateField(
		verbose_name='Incluído',
		null=True, blank=True
	)
	excluded = models.DateField(
		verbose_name='Excluído',
		null=True, blank=True
	)
	created_at = models.DateTimeField(
		verbose_name='Criado em',
		null=True, blank=True,
		auto_now_add=True
	)
	updated_at = models.DateTimeField(
		verbose_name='Atualizado em',
		null=True, blank=True,
		auto_now=True
	)

	def __str__(self):
		return f'{self.name} - {self.matriculation}'

	class Meta:
		verbose_name='Sentenciado'
		verbose_name_plural='Sentenciados'
		ordering=['included']
