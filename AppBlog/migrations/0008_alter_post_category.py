# Generated by Django 4.0.4 on 2022-10-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0007_alter_comment_options_comment_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Fiction', 'Fiction'), ('Sports', 'Sports'), ('Thriller', 'Thriller'), ('Shounen', 'Shounen'), ('Fantasy', 'Fantasy')], max_length=20, null=True),
        ),
    ]
