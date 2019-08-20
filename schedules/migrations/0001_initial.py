# Generated by Django 2.2.2 on 2019-06-17 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20190617_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Hora de inicio')),
                ('end_time', models.TimeField(verbose_name='Hora de finalización')),
                ('day', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado')], max_length=30, verbose_name='Día')),
                ('type', models.CharField(choices=[('Calendar', 'Calendar'), ('Solicitude', 'Solicitude')], max_length=30, verbose_name='Tipo de franja horaria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Franja horaria',
                'verbose_name_plural': 'Franjas horarias',
            },
        ),
    ]