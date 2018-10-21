# Generated by Django 2.1.2 on 2018-10-21 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('russianseasons', '0010_auto_20181021_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='sold',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
