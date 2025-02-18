# Generated by Django 4.2.14 on 2024-08-05 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/playlists/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='musics', to='spot.album'),
        ),
        migrations.AlterField(
            model_name='music',
            name='history',
            field=models.ManyToManyField(blank=True, related_name='history_music', through='spot.History', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='music',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_musics', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
