# Generated by Django 3.1.7 on 2021-03-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0006_auto_20200129_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaunaBait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_ingredient_name'),
        ),
        migrations.AddConstraint(
            model_name='faunabait',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_faunabait_name'),
        ),
    ]