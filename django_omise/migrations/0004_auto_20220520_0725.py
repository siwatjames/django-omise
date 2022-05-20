# Generated by Django 3.2.13 on 2022-05-20 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_omise', '0003_refund'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='default_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='django_omise.card'),
        ),
        migrations.AddField(
            model_name='customer',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, help_text='Custom metadata for this customer.'),
        ),
    ]