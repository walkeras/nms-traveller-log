# Generated by Django 3.0.1 on 2020-07-26 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0010_auto_20200514_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='world',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
    ]
