# Generated by Django 2.1.2 on 2018-10-21 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('russianseasons', '0014_auto_20181021_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10000)),
                ('email', models.CharField(default='', max_length=10000)),
                ('text', models.TextField()),
            ],
        ),
    ]
