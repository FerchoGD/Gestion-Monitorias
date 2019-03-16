from django.db import models

# Create your models here.
class Admin(models.Model):
    id_admin = models.SmallIntegerField(verbose_name="Id", default=0)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    last_name = models.CharField(verbose_name="Apellidos", max_length=200)
    email = models.EmailField(verbose_name="Email",max_length=100,blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        ordering = ['id_admin', 'last_name']

    def __str__(self):
        return self.name
