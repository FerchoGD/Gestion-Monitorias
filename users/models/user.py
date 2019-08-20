from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

TYPES_USERS = [
    ('Superuser','Superuser'),
    ('Admin','Admin'),
    ('Student','Student'),
    ('Monitor','Monitor')
]

class User(models.Model):
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Usuario'
    )
    dni = models.CharField(max_length=30)
    type_user = models.CharField(max_length=30, choices=TYPES_USERS)
    subject_assigned = models.ManyToManyField(
        'subjects.Subject',
        verbose_name='Asignaturas asignadas',
        blank=True
    )
    image_profile = models.ImageField(upload_to='static/img/profile/', blank=True, null=True)
    hours = models.IntegerField(verbose_name='Horas por cumplir',default=0)
    birth_date = models.DateField(verbose_name='Fecha de nacimiento',default=timezone.now())
    gender = models.CharField(max_length=30,default='Masculino')

    def __str__(self):
        return str(self.user)
