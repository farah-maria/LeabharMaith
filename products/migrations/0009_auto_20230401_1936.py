# Generated by Django 3.2 on 2023-04-01 19:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230324_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured_product',
            name='extra_image1',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='featured_product',
            name='extra_image2',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]