# Generated by Django 2.1.5 on 2019-01-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sub_location',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sub_location',
            name='sub_location_number',
            field=models.CharField(max_length=100),
        ),
    ]
