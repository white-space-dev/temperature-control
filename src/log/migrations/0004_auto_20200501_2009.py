# Generated by Django 3.0.5 on 2020-05-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20200501_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='date_temp_taken',
            field=models.DateField(auto_now_add=True),
        ),
    ]
