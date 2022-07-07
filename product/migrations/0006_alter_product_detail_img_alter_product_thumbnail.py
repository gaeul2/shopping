# Generated by Django 4.0.5 on 2022-07-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_detail_img_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail_img',
            field=models.FileField(upload_to='images/product/detail'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(upload_to='images/product/thumbnail'),
        ),
    ]
