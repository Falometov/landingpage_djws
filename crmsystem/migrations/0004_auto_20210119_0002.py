# Generated by Django 3.1.5 on 2021-01-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmsystem', '0003_auto_20210118_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_value',
            field=models.CharField(max_length=200, verbose_name='Value'),
        ),
    ]
