# Generated by Django 5.1.7 on 2025-04-13 22:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='job',
            index=models.Index(fields=['title'], name='job_title_idx'),
        ),
    ]
