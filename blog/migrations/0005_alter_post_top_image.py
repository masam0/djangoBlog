# Generated by Django 4.0.6 on 2022-07-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_top_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='top_image',
            field=models.FilePathField(blank=True, null=True),
        ),
    ]