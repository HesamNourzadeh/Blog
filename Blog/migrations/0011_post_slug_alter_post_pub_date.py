# Generated by Django 5.0.1 on 2024-03-13 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_alter_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 13, 13, 30, 18, 276440, tzinfo=datetime.timezone.utc)),
        ),
    ]
