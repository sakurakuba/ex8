# Generated by Django 4.1 on 2022-08-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pr_img',
            field=models.ImageField(blank=True, default='review/static/default_img/default.jpeg', null=True, upload_to='pr_images', verbose_name='Product Image'),
        ),
    ]
