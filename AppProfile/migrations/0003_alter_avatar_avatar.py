# Generated by Django 4.0.4 on 2022-10-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfile', '0002_alter_avatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/avatardefault.png', null=True, upload_to='avatars/'),
        ),
    ]