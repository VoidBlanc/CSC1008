# Generated by Django 4.0.3 on 2022-03-24 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIFT', '0003_pointinfo_highway'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathCache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.IntegerField()),
                ('destination', models.IntegerField()),
                ('Data', models.TextField(null=True)),
                ('DateTime', models.DateTimeField()),
            ],
        ),
    ]
