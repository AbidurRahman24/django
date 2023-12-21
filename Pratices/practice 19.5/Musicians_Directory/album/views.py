from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            messages.success(request, 'Added Album Successfully')
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()
    # print(album_form)
    return render(request, 'add_album.html', {'form' : album_form})
# class base view 
# add album
@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):

    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        messages.success(self.request, 'Added Album Successfully')
        return super().form_valid(form)


@login_required
def edit_album(request, id):
    album = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album) 
        if album_form.is_valid(): 
            album_form.save()
            return redirect('homepage') 
    return render(request, 'add_album.html', {'form' : album_form})


# class base edit
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('add_album')

