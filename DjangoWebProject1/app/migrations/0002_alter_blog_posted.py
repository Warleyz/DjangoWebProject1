# Generated by Django 4.2.7 on 2023-11-21 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 11, 22, 0, 28, 52, 404902), verbose_name='Опубликована'),
        ),
    ]
