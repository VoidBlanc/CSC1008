# Generated by Django 4.0.3 on 2022-03-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIFT', '0005_alter_pathcache_destination_alter_pathcache_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointinfo',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pointinfo',
            name='long',
            field=models.FloatField(default=0),
        ),
    ]
