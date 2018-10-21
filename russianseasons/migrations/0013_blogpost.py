# Generated by Django 2.1.2 on 2018-10-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('russianseasons', '0012_order_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
