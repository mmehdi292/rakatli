# Generated by Django 3.0.8 on 2020-07-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_core', '0011_auto_20200727_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='s',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='HTML',
            field=models.TextField(default='', null=True),
        ),
    ]
