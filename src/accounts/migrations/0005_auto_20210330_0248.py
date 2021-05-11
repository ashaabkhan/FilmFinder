# Generated by Django 3.1.7 on 2021-03-30 06:48

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/blank_avatar.png', null=True, upload_to=accounts.models.upload_image_path),
        ),
    ]
