# Generated by Django 3.0.5 on 2020-05-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_auto_20200501_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='date_joined',
            field=models.DateField(blank=True, null=True),
        ),
    ]
