# Generated by Django 2.1.7 on 2019-03-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20190302_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/default_img/default.png', upload_to='products_images'),
        ),
    ]