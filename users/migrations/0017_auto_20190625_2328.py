# Generated by Django 2.2.2 on 2019-06-26 04:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190625_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2019, 6, 26, 4, 28, 20, 808320, tzinfo=utc), verbose_name='Fecha de nacimiento'),
        ),
    ]
