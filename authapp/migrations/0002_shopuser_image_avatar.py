# Generated by Django 2.1.7 on 2019-03-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='image_avatar',
            field=models.ImageField(blank=True, default='/image_avatar/default.png', upload_to='image_avatar'),
        ),
    ]
