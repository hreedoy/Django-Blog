# Generated by Django 3.2 on 2021-05-18 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profie_picture',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
