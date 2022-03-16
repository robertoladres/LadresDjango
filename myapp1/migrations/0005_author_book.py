# Generated by Django 3.2.6 on 2021-09-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0004_auto_20210922_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_Id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('birthdate', models.CharField(max_length=10)),
                ('mobilenumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('year_published', models.IntegerField()),
            ],
        ),
    ]
