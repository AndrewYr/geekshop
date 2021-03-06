# Generated by Django 2.1.7 on 2019-03-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_shopuser_image_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuser',
            name='image_avatar',
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='avatar',
            field=models.ImageField(blank=True, default='/image_avatar/default.png', upload_to='users_avatars'),
        ),
    ]
