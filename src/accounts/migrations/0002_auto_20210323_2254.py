# Generated by Django 3.1.6 on 2021-03-24 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='actives',
            new_name='active',
        ),
    ]
