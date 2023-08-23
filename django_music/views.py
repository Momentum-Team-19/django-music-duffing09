from django.shortcuts import render

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})