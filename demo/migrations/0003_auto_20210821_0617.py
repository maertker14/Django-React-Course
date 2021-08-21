# Generated by Django 3.2.6 on 2021-08-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20210821_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=206),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]