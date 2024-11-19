# Generated by Django 5.1.3 on 2024-11-19 06:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='time plublished'),
            preserve_default=False,
        ),
    ]
