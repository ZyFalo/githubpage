# Generated by Django 5.1.6 on 2025-03-08 23:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
