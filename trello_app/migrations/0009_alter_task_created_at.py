# Generated by Django 5.2.1 on 2025-07-28 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0008_alter_task_created_at_alter_tasklist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 28, 9, 42, 3, 640434, tzinfo=datetime.timezone.utc)),
        ),
    ]
