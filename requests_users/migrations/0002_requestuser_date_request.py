# Generated by Django 2.2.2 on 2019-06-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestuser',
            name='date_request',
            field=models.DateField(auto_now=True, verbose_name='Fecha de solicitud'),
        ),
    ]
