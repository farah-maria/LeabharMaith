# Generated by Django 3.2 on 2023-04-04 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='genre',
            new_name='name',
        ),
    ]
