# Generated by Django 4.0.6 on 2024-05-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0006_band_biografia_band_imagem_music_letra'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='app/fotos'),
        ),
    ]
