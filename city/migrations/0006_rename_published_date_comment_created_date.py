# Generated by Django 4.2.3 on 2023-07-14 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='published_date',
            new_name='created_date',
        ),
    ]