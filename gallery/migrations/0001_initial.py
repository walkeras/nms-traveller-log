# Generated by Django 3.0.1 on 2020-07-27 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('worlds', '0011_world_favourite'),
        ('systems', '0017_system_near_system_dist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(max_length=20, null=True)),
                ('description', models.TextField(blank=True)),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('type', models.CharField(choices=[('Alien Monolith', 'Alien Monolith'), ('Space Anomaly', 'Space Anomaly'), ('Fauna', 'Fauna'), ('Flora', 'Flora'), ('Landscape', 'Landscape'), ('Miscellaneous', 'Miscellaneous')], max_length=30)),
                ('system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='systems.System')),
                ('world', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='worlds.World')),
            ],
        ),
    ]
