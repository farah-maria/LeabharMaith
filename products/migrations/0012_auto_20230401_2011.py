# Generated by Django 3.2 on 2023-04-01 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20230401_1941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featured_product',
            old_name='featured_image1',
            new_name='advert_image1',
        ),
        migrations.RenameField(
            model_name='featured_product',
            old_name='featured_image2',
            new_name='advert_image2',
        ),
        migrations.RenameField(
            model_name='featured_product',
            old_name='extra_image1_url',
            new_name='image1_url',
        ),
        migrations.RenameField(
            model_name='featured_product',
            old_name='extra_image2_url',
            new_name='image2_url',
        ),
    ]
