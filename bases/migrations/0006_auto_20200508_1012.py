# Generated by Django 3.0.1 on 2020-05-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0005_auto_20200103_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='description',
            field=models.TextField(blank=True, help_text="Use the pipe '|' character to list multiple items"),
        ),
    ]