# Generated by Django 5.1.4 on 2025-03-18 08:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('item_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(blank=True, default=False)),
                ('dead', models.BooleanField(blank=True, default=False)),
                ('type', models.CharField(choices=[('job', 'Job'), ('story', 'Story'), ('comment', 'Comment'), ('poll', 'Poll'), ('pollopt', 'Pollopt')], max_length=10)),
                ('score', models.IntegerField(blank=True, default=0)),
                ('descendants', models.IntegerField(blank=True, default=0)),
                ('url', models.URLField(blank=True, default='https://news.ycombinator.com/')),
                ('text', models.TextField(blank=True, default='')),
                ('title', models.TextField()),
            ],
            options={
                'db_table': 'jobs',
                'ordering': ('-time', '-score'),
                'permissions': [('can_edit', 'can edit job posting')],
                'abstract': False,
            },
        ),
    ]
