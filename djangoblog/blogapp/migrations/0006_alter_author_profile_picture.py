# Generated by Django 3.2 on 2021-05-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_rename_profie_picture_author_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
