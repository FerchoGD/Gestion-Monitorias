# Generated by Django 2.1.7 on 2019-03-24 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfiles', '0004_admin_advisor_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_subject', models.SmallIntegerField(default=0, verbose_name='Id')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advisor', to='perfiles.Advisor')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
                'ordering': ['id_subject', 'name'],
            },
        ),
    ]
