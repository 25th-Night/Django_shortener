# Generated by Django 3.2.13 on 2023-01-24 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20230121_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='custom_params',
            field=models.JSONField(null=True),
        ),
        migrations.CreateModel(
            name='TrackingParams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('params', models.CharField(max_length=20)),
                ('shortened_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.shortenedurls')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
