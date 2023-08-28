from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import AlbumForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# retrieves all album objects from database using line 9 and passes them to 'album_list.html' using render function
@login_required
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


# takes 'pk' which is primary key of the album to be displayed. retrieves album object using line 15 and passes it to 'album_detail.html'
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


# handles creation of new album. if request is post, it validates submitted form using line 22. if form is valid saves data to database and creates an album object
def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_new.html', {'form': form})


# handles editing an album. retrieves album object based on pk. if request is post, validates form with updated data and saves. then redirects to album list.
def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_edit.html', {'form': form})


# handles deletion of an album. retrieves album based on pk, then calls delete method on album object to remove it from database, redirects to album list
def album_remove(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')

# these functions define the various views required for managing albums in a web abblication. they interact with the database through django models, validate form data, and render templates to display album information