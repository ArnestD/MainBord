# Generated by Django 4.2.3 on 2023-07-18 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_coment_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
