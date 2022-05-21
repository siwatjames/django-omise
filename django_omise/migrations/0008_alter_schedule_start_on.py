# Generated by Django 3.2.13 on 2022-05-21 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_omise', '0007_charge_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='start_on',
            field=models.DateField(help_text='Start date of schedule in ISO 8601 format.'),
        ),
    ]
