# Generated by Django 4.1.4 on 2022-12-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(choices=[('В наличии', 'In Stock'), ('Под заказ', 'For Order'), ('Ожидается', 'Waiting'), ('Нет в наличии', 'Not In Stock'), ('Не производится', 'Not Producing')], default='В наличии')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
    ]