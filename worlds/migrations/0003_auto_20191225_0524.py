# Generated by Django 3.0.1 on 2019-12-25 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0004_auto_20191224_1123'),
        ('worlds', '0002_auto_20191225_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='world',
            name='resource_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_1', to='reference.Resource'),
        ),
        migrations.AlterField(
            model_name='world',
            name='resource_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_2', to='reference.Resource'),
        ),
        migrations.AlterField(
            model_name='world',
            name='resource_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_3', to='reference.Resource'),
        ),
        migrations.AlterField(
            model_name='world',
            name='resource_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_4', to='reference.Resource'),
        ),
        migrations.AlterField(
            model_name='world',
            name='resource_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_5', to='reference.Resource'),
        ),
        migrations.AlterField(
            model_name='world',
            name='resource_6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='resource_6', to='reference.Resource'),
        ),
    ]
