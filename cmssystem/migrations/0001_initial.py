# Generated by Django 3.1.5 on 2021-01-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmsSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cms_img', models.ImageField(upload_to='sliderimg/')),
                ('cms_title', models.CharField(max_length=200, verbose_name='Title')),
                ('cms_text', models.CharField(max_length=500, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
    ]