# Generated by Django 3.0.5 on 2020-05-11 07:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0011_auto_20200511_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='date_temp_taken',
            field=models.DateField(default=datetime.datetime(2020, 5, 11, 7, 21, 6, 740790), unique=True),
        ),
    ]
