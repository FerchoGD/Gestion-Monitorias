from django.db import models

class Subject(models.Model):
    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    code = models.CharField(
        max_length=10,
        verbose_name='Código'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre'
    )

    def __str__(self):
        return self.name
