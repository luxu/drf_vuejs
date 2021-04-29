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
		return f'{self.matriculation} - {self.name}'

	class Meta:
		verbose_name='Sentenciado'
		verbose_name_plural='Sentenciados'
