# Generated by Django 4.2.1 on 2023-05-11 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response_forum', '0006_alter_response_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 11, 15, 3, 46, 273113, tzinfo=datetime.timezone.utc)),
        ),
    ]
