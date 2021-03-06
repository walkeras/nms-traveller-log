# Generated by Django 3.0.1 on 2020-06-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0015_auto_20200604_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='system',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='system',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='system',
            name='black_hole',
            field=models.BooleanField(default=False, help_text='Black Hole present in this system'),
        ),
    ]
