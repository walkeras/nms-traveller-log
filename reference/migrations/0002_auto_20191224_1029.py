# Generated by Django 3.0.1 on 2019-12-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economylevel',
            name='level',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1),
        ),
    ]
