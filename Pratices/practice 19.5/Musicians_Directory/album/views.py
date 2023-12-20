from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
        
    else:
        album_form = forms.AlbumForm()
    return render(request, 'album.html', {'form' : album_form})


def edit_album(request, id):
    album = models.Album.objects.get(pk=id) 
    album_form = forms.AlbumForm(instance=album)

    if request.method == 'POST':
        album_form = forms.MusicianForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    
    return render(request, 'album.html', {'form' : album_form})

def delete_musician(request, id):
    album = models.Album.objects.get(pk=id) 
    album.delete()
    return redirect('homepage')