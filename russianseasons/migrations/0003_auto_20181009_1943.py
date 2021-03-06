# Generated by Django 2.0.6 on 2018-10-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('russianseasons', '0002_itemprototype_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprototype',
            name='categories',
            field=models.ManyToManyField(null=True, to='russianseasons.Category'),
        ),
        migrations.AlterField(
            model_name='itemprototype',
            name='colors',
            field=models.ManyToManyField(null=True, to='russianseasons.Color'),
        ),
        migrations.AlterField(
            model_name='itemprototype',
            name='description',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='itemprototype',
            name='images',
            field=models.ManyToManyField(null=True, to='russianseasons.Image'),
        ),
        migrations.AlterField(
            model_name='itemprototype',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='itemprototype',
            name='sizes',
            field=models.ManyToManyField(null=True, to='russianseasons.Size'),
        ),
    ]
