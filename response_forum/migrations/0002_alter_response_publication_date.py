# Generated by Django 4.2 on 2023-04-30 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response_forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 30, 15, 20, 22, 112518, tzinfo=datetime.timezone.utc)),
        ),
    ]
