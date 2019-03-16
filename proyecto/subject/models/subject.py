from django.db import models
from perfiles.models.advisor import Advisor



class Subject(models.Model):
    id_subject = models.SmallIntegerField(verbose_name="Id", default=0)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
        ordering = ['id_subject', 'name']

    def __str__(self):
        return self.name
