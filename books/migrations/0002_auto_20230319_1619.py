# Generated by Django 3.2 on 2023-03-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name1',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name1',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
