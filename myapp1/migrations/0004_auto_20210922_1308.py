# Generated by Django 3.2.6 on 2021-09-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_auto_20210914_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='Username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]