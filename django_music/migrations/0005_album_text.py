# Generated by Django 4.2.4 on 2023-08-23 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_music', '0004_alter_song_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
