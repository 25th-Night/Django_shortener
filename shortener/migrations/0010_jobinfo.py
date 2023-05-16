# Generated by Django 3.2.13 on 2023-05-07 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0009_dailyvisitors'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job_id', models.CharField(max_length=255)),
                ('user_id', models.IntegerField(null=True)),
                ('additional_info', models.JSONField(null=True)),
                ('status', models.CharField(choices=[('wait', 'Wait'), ('run', 'Run'), ('ok', 'Ok'), ('error', 'Error')], default='wait', max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
