from django.db import models

DAYS = [
    ('Lunes','Lunes'),
    ('Martes','Martes'),
    ('Miércoles','Miércoles'),
    ('Jueves','Jueves'),
    ('Viernes','Viernes'),
    ('Sábado','Sábado')
]

TYPES_TIMESSLOTS = [
    ('Calendar','Calendar'),
    ('Solicitude','Solicitude')
]

class TimeSlot(models.Model):
    class Meta:
        verbose_name = 'Franja horaria'
        verbose_name_plural = 'Franjas horarias'

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Usuario'
    )
    start_time = models.TimeField(
        verbose_name='Hora de inicio'
    )
    end_time = models.TimeField(
        verbose_name='Hora de finalización'
    )
    day = models.CharField(
        max_length=30,
        verbose_name='Día',
        choices=DAYS,
        null=True
    )
    type = models.CharField(
        max_length=30,
        verbose_name='Tipo de franja horaria',
        choices=TYPES_TIMESSLOTS
    )

    def __str__(self):
        return 'Franja horaria de %s' % str(self.user)
