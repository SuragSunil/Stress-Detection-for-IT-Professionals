# Generated by Django 5.1.6 on 2025-03-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_resource_alert_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='triggered_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
