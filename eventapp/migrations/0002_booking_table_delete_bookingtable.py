# Generated by Django 5.1.4 on 2025-01-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.CharField(max_length=20)),
                ('event_date', models.DateField()),
                ('guests', models.IntegerField()),
                ('venue', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='BookingTable',
        ),
    ]
