# Generated by Django 4.0.6 on 2024-05-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_infoadicionaluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigos',
            name='categoria',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artigos',
            name='introducao',
            field=models.TextField(blank=True, null=True),
        ),
    ]