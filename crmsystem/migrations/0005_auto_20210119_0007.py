# Generated by Django 3.1.5 on 2021-01-18 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmsystem', '0004_auto_20210119_0002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='request_value',
            new_name='request_plan',
        ),
    ]
