# Generated by Django 3.0.1 on 2020-01-03 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0003_auto_20200103_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='portal_address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]