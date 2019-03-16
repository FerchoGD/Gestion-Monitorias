from django.db import models
from subject.models.subject import Subject


class Student(models.Model):
    id_student = models.SmallIntegerField(verbose_name="Id", default=0)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    last_name = models.CharField(verbose_name="Apellidos", max_length=200)
    email = models.EmailField(verbose_name="Email",max_length=100,blank=True)
    birthdate = models.DateTimeField(verbose_name="Fecha de nacimiento")
    gender = models.CharField(verbose_name="Genero", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    subjects = models.ManyToManyField(Subject)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering  = ['id_student','last_name']

    def __str__(self):
        return self.name