# Generated by Django 4.0.6 on 2022-07-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_date_published_alter_post_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(verbose_name='date updated'),
        ),
    ]