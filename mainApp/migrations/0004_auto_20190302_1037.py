# Generated by Django 2.1.7 on 2019-03-02 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20190302_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/products_images/product-41_2RB71EP.jpg', upload_to='products_images'),
        ),
    ]
