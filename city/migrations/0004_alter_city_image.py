# Generated by Django 4.2.3 on 2023-07-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0003_city_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(upload_to='city/photos'),
        ),
    ]