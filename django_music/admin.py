from django.contrib import admin
from .models import User, Artist, Song, Album

admin.site.register(Artist)
admin.site.register(User)
admin.site.register(Song)
admin.site.register(Album)