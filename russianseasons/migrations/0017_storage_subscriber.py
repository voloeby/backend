# Generated by Django 2.1.2 on 2018-10-21 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('russianseasons', '0016_auto_20181021_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=100)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
