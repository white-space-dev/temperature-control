# Generated by Django 3.0.5 on 2020-04-27 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('date_joined', models.DateField()),
                ('date_signedoff', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.DecimalField(decimal_places=2, max_digits=4)),
                ('time_temp_taken', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=20)),
                ('date_temp_taken', models.DateField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Personnel')),
            ],
        ),
    ]
