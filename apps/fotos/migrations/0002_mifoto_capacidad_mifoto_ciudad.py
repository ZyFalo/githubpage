# Generated by Django 5.1.6 on 2025-03-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mifoto',
            name='capacidad',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mifoto',
            name='ciudad',
            field=models.CharField(default='Colombia', max_length=100),
            preserve_default=False,
        ),
    ]
