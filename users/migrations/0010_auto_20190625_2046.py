# Generated by Django 2.2.2 on 2019-06-26 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190625_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hours',
            field=models.IntegerField(blank=True, verbose_name='horas por cumplir'),
        ),
    ]
