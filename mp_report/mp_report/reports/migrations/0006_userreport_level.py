# Generated by Django 4.2.6 on 2024-02-15 07:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_remove_tag_data_value_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreport',
            name='level',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)]),
        ),
    ]
