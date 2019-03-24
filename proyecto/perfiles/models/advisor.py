from django.db import models

class Advisor(models.Model):
    id_advisor = models.SmallIntegerField(verbose_name="Id", default=0)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    last_name = models.CharField(verbose_name="Apellidos", max_length=200)
    birthdate = models.DateTimeField(verbose_name="Fecha de nacimiento")
    gender = models.CharField(verbose_name="Genero", max_length=200)
    hours = models.SmallIntegerField(verbose_name="Horas Asignadas", default=0)
    subject = models.CharField(verbose_name="Materia asignada", max_length=200)
    email = models.EmailField(verbose_name="Email",max_length=100,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    estudiantes = models.ManyToManyField('perfiles.Student', related_name='Estudiantes')

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitores"
        ordering  = ['id_advisor','last_name']

    def __str__(self):
        return self.name
