# Generated by Django 3.0.1 on 2020-01-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0004_world_photo_marquee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='world',
            name='description',
            field=models.CharField(blank=True, help_text='From Starship Scan', max_length=50),
        ),
        migrations.AlterField(
            model_name='world',
            name='fauna_desc',
            field=models.CharField(blank=True, help_text='From Discovery Data', max_length=20),
        ),
        migrations.AlterField(
            model_name='world',
            name='fauna_hostility_desc',
            field=models.CharField(blank=True, help_text='Additional description, eg. Frequent Attacks, Occasional Attacks', max_length=50),
        ),
        migrations.AlterField(
            model_name='world',
            name='fauna_hostility_level',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low'), ('U', 'Unknown')], default='U', help_text='Low - No attacks. Medium - Occasional Attacks. High - Frequent Attacks.', max_length=1),
        ),
        migrations.AlterField(
            model_name='world',
            name='flora_desc',
            field=models.CharField(blank=True, help_text='From Discovery Data', max_length=20),
        ),
        migrations.AlterField(
            model_name='world',
            name='resources_notes',
            field=models.TextField(blank=True, help_text='Additional notes, eg. Ancient Bones, Tech Modules, resource occurrence frequency'),
        ),
        migrations.AlterField(
            model_name='world',
            name='sentinel_desc',
            field=models.CharField(blank=True, help_text='From Discovery Data', max_length=30),
        ),
        migrations.AlterField(
            model_name='world',
            name='sentinel_hostility_desc',
            field=models.CharField(blank=True, help_text='Additional description, eg. Frequent Attacks, Attack on sight', max_length=50),
        ),
        migrations.AlterField(
            model_name='world',
            name='sentinel_hostility_level',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low'), ('U', 'Unknown')], default='U', help_text='Low - Normal/Low presence. Medium - Frequent scans/High presence. High - Attack on sight.', max_length=1),
        ),
        migrations.AlterField(
            model_name='world',
            name='weather_desc',
            field=models.CharField(blank=True, help_text='From Discovery Data', max_length=50),
        ),
        migrations.AlterField(
            model_name='world',
            name='weather_notes',
            field=models.CharField(blank=True, help_text='Additional description, eg. Frequent Storms, Occasional Storms', max_length=50),
        ),
        migrations.AlterField(
            model_name='world',
            name='weather_rating',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low'), ('U', 'Unknown')], default='U', help_text='Low - Day/Night Only hazard with Infrequent Storms. Medium - Constant hazard. High - Frequent Storms or Extreme World.', max_length=1),
        ),
    ]
