# Generated by Django 3.1.3 on 2020-11-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]