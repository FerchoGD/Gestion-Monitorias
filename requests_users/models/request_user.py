from django.db import models

from datetime import datetime

REQUEST_STATES = [
    ('Requested', 'Requested'),
    ('Accepted', 'Accepted'),
    ('Declined', 'Declined'),
    ('FinishedMonitor', 'FinishedMonitor'),
    ('FinishedEstudent', 'FinishedEstudent')
]

class RequestUser(models.Model):
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        # ordering = ['state']

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Estudiante',
        related_name='Estudiante',
        blank=False
    )
    monitor = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Monitor',
        related_name='Monitor',
        blank=False
    )
    requested_time = models.DateField(
        verbose_name='Fecha de solicitud',
        default=datetime.now
    )
    time_slot = models.ForeignKey(
        'schedules.TimeSlot',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Franja horaria de la solicitud'
    )
    subject = models.ForeignKey(
        'subjects.Subject',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Asignatura'
    )
    state = models.CharField(
        max_length=30,
        verbose_name='Estado de la solicitud',
        choices=REQUEST_STATES
    )

    def __str__(self):
        return 'Solicitud #%i de %s' % (self.pk, self.user)

# ED7A07D74B8B5C7F0CB04A9BE11B89C886FB73D3