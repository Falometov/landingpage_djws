# Generated by Django 3.1.5 on 2021-01-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmssystem', '0002_auto_20210118_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS class'),
        ),
    ]
