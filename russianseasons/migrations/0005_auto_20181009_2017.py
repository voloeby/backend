# Generated by Django 2.0.6 on 2018-10-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('russianseasons', '0004_auto_20181009_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
