# Generated by Django 4.2.5 on 2023-09-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summoner_search', '0003_summoner_summonerlevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='summoner',
            name='tier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
