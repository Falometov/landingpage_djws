# Generated by Django 3.1.5 on 2021-01-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_dt', models.DateTimeField(auto_now=True)),
                ('request_name', models.CharField(max_length=200, verbose_name='Name')),
                ('request_email', models.EmailField(max_length=200, verbose_name='Email')),
                ('request_plan', models.CharField(max_length=200, verbose_name='Plan')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
    ]