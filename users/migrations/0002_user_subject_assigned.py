# Generated by Django 2.2.2 on 2019-06-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subject_assigned',
            field=models.ManyToManyField(to='subjects.Subject', verbose_name='Asignaturas asignadas'),
        ),
    ]
