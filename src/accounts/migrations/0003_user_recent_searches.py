# Generated by Django 3.1.7 on 2021-03-24 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210323_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='recent_searches',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
