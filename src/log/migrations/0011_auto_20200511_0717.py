# Generated by Django 3.0.5 on 2020-05-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0010_auto_20200511_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temp_PM',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
