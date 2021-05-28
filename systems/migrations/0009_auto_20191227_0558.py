# Generated by Django 3.0.1 on 2019-12-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0008_auto_20191227_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='star_colour',
            field=models.CharField(blank=True, choices=[('Yellow', 'Yellow'), ('Red', 'Red'), ('Green', 'Green'), ('Blue', 'Blue'), ('Unknown', 'Unknown')], default='Unknown', max_length=7),
        ),
    ]
