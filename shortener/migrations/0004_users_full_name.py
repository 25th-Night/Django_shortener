# Generated by Django 3.2.13 on 2022-10-17 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_delete_userdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
