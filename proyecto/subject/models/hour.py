from django.db import models
from perfiles.models.advisor import Advisor
from perfiles.models.student import Student
from subject.models import Subject


class Hour(models.Model):
    id_hour = models.SmallIntegerField(verbose_name="Id", default=0)
    hora = models.TimeField(verbose_name="Hora")
    day = models.CharField(verbose_name="Nombre", max_length=200)
    num_students = models.SmallIntegerField(verbose_name="Id", default=0)
    date = models.DateTimeField(verbose_name="Fecha")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)


    class Meta:
        verbose_name = "Hora"
        verbose_name_plural = "Horas"
        ordering = ['id_hour', 'hora']

    def __str__(self):
        return self.hora
