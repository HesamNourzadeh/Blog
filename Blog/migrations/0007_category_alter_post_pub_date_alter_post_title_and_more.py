# Generated by Django 5.0.1 on 2024-02-18 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_post_pub_date_alter_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 18, 10, 26, 1, 882063, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='Blog.category'),
        ),
    ]
