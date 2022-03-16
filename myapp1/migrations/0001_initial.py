# Generated by Django 3.2.6 on 2021-09-14 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdminId', models.CharField(max_length=10)),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerId', models.CharField(max_length=10)),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('ContactNum', models.IntegerField(max_length=11)),
                ('Street', models.CharField(max_length=20)),
                ('City_Municipality', models.CharField(max_length=20)),
                ('Province', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderId', models.CharField(max_length=10)),
                ('BookId', models.CharField(max_length=10)),
                ('Quantity', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('TotalAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookId', models.CharField(max_length=10)),
                ('BookTitle', models.CharField(max_length=10)),
                ('Author', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SeqId', models.IntegerField()),
                ('Quantity', models.IntegerField()),
                ('Date', models.DateField()),
                ('BookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.stocks')),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp1.order')),
            ],
        ),
    ]
