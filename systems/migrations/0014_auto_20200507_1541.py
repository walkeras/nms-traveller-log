# Generated by Django 3.0.1 on 2020-05-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0013_auto_20200129_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='comments',
            field=models.TextField(blank=True, help_text="Use the pipe '|' character to list multiple items"),
        ),
    ]
