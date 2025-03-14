# Generated by Django 5.1.6 on 2025-03-04 04:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_applicationusage_keyboardactivity_screentime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('VIDEO', 'Video'), ('ARTICLE', 'Article'), ('AUDIO', 'Audio'), ('EXERCISE', 'Exercise')], max_length=50)),
                ('url', models.URLField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='resources/')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='Alert message for high stress')),
                ('threshold', models.IntegerField(help_text='Stress score threshold that triggered this alert')),
                ('triggered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_acknowledged', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usersregister')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_text', models.TextField(help_text='Personalized recommendation content')),
                ('category', models.CharField(choices=[('BREAK', 'Take a Break'), ('EXERCISE', 'Exercise'), ('MINDFULNESS', 'Mindfulness'), ('SCHEDULE', 'Schedule Adjustment'), ('RESOURCE', 'Resource')], max_length=50)),
                ('priority', models.IntegerField(default=1, help_text='Priority level (1-5)')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_completed', models.BooleanField(default=False)),
                ('stress_assessment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.stressassessment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usersregister')),
            ],
        ),
    ]
