# Generated by Django 2.2.4 on 2020-12-31 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Username', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('EventStart', models.CharField(max_length=255)),
                ('EventEnd', models.CharField(max_length=255)),
                ('Plan', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('PossibleTrips', models.ManyToManyField(related_name='possible_places', to='eventsData.User')),
                ('Traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PlacesToVisit', to='eventsData.User')),
            ],
        ),
    ]
