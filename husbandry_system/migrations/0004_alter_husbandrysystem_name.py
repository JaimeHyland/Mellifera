# Generated by Django 5.0.7 on 2024-12-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('husbandry_system', '0003_alter_husbandrysystem_depth_deep_mm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='husbandrysystem',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
