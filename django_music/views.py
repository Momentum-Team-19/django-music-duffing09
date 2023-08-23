from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


def album_new(request):
    form = AlbumForm()
    return render(request, 'album_edit.html', {'form': form})