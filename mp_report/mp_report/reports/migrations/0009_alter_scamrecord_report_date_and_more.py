# Generated by Django 4.2.6 on 2024-02-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_scamrecord_alter_userreport_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scamrecord',
            name='report_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='scamrecord',
            name='scam_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
