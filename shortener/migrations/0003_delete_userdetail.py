# Generated by Django 3.2.13 on 2022-10-17 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_userdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]
