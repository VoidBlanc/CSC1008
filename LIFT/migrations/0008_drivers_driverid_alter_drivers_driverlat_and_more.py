# Generated by Django 4.0.3 on 2022-03-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIFT', '0007_drivers'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='driverID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='driverlat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='driverlong',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drivers',
            name='seatNo',
            field=models.IntegerField(default=0),
        ),
    ]
