# Generated by Django 3.2.13 on 2022-05-20 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_omise', '0004_auto_20220520_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, help_text='Custom metadata for this object.'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, help_text='Custom metadata for this object.'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, help_text='Custom metadata for this object.'),
        ),
    ]
