# Generated by Django 2.1.7 on 2019-03-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='mainApp/static/img/default.png', upload_to='products_images'),
        ),
    ]