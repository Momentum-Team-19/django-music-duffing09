# models imported, used to define your data models(artist,album,song)
from django.db import models
# abstractuser is a base class provided by django for extending default user model
from django.contrib.auth.models import AbstractUser
# Create your models here.


# defines artist model. single field 'name'
class Artist(models.Model):
    name = models.CharField(max_length=100)
    # defined to specify artist should be a string. returns 'name' attribute of artist

    def __str__(self) -> str:
        return self.name


# defines album model with several fields
class Album(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="albums")
# defines album represented as a string. returns the 'title' attribute of the album

    def __str__(self) -> str:
        return self.title


# defines a 'Song' model
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=150)
    duration = models.DurationField(blank=True, null=True)

# defines a 'Song' object should be a string
    def __str__(self) -> str:
        return self.title


# extends django's 'abstractuser' model, which provides basic fields and methods for a user in the authentication system
class User(AbstractUser):
    pass
