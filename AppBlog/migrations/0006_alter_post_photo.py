# Generated by Django 4.0.4 on 2022-10-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0005_alter_comment_content_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='images/no_image.jpg', null=True, upload_to='images', verbose_name='Foto'),
        ),
    ]