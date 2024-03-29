# Generated by Django 2.2.2 on 2019-06-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
        ('users', '0003_auto_20190617_1101'),
        ('subjects', '0002_auto_20190617_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Requested', 'Requested'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=30, verbose_name='Estado de la solicitud')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Monitor', to='users.User', verbose_name='Monitor')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.Subject', verbose_name='Asignatura')),
                ('time_slot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedules.TimeSlot', verbose_name='Franja horaria de la solicitud')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Estudiante', to='users.User', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
            },
        ),
    ]
