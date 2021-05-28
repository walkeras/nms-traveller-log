# Generated by Django 3.0.1 on 2020-08-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0017_system_near_system_dist'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='derelict_freighter_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='system',
            name='derelict_freighter_notes',
            field=models.TextField(blank=True),
        ),
    ]