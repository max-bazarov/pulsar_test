# Generated by Django 4.1.4 on 2022-12-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_extension_image_remove_product_image_productimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='imageextension',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='imageextension',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.DeleteModel(
            name='Extension',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='ImageExtension',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
