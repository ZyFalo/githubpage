# Generated by Django 5.1.6 on 2025-03-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_noticia_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
