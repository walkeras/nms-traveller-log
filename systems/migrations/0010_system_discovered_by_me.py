# Generated by Django 3.0.1 on 2019-12-28 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0009_auto_20191227_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='discovered_by_me',
            field=models.BooleanField(default=True),
        ),
    ]
