# Generated by Django 4.1.4 on 2022-12-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('in stock', 'В наличии'), ('for order', 'Под заказ'), ('waiting', 'Ожидается'), ('not in stock', 'Нет в наличии'), ('not producing', 'Не производится')], default='in stock', max_length=255),
        ),
    ]
