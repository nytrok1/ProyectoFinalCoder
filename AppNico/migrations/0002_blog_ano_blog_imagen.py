# Generated by Django 4.2.5 on 2023-10-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppNico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='ano',
            field=models.IntegerField(default=2023),
        ),
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/imagen/'),
        ),
    ]
