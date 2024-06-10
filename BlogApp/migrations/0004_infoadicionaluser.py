# Generated by Django 4.0.6 on 2024-05-29 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0003_alter_artigos_autor_alter_comentariorating_autor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='infoAdicionalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='app/fotos')),
                ('biografia', models.TextField(blank=True, null=True)),
                ('dataNascimento', models.DateTimeField(blank=True, null=True)),
                ('interesses', models.TextField()),
                ('profissao', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infoAdicionalUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]