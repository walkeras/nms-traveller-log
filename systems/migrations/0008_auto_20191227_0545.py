# Generated by Django 3.0.1 on 2019-12-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0007_system_discovered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='race',
            field=models.CharField(choices=[('Gek', 'Gek'), ('Korvax', 'Korvax'), ('Vykeen', 'Vykeen'), ('Uncharted', 'Uncharted')], max_length=9),
        ),
    ]