# Generated by Django 3.0.5 on 2020-05-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0007_auto_20200507_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperature',
            name='temp_AM',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='temp_PM',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
