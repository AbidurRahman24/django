from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
# Create your views here.
@login_required
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : musician_form})


@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        messages.success(self.request, 'Added Musician Successfully')
        return super().form_valid(form)


@login_required
def edit_musician(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician) 
        if musician_form.is_valid(): 
            musician_form.save()
            return redirect('homepage') 
    return render(request, 'add_musician.html', {'form' : musician_form})


@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

@login_required
def delete_musician(request, id):
    musician = models.Musician.objects.get(pk=id) 
    musician.delete()
    return redirect('homepage')

@method_decorator(login_required, name='dispatch')
class DeletemusicianView(DeleteView):
    model = models.Musician
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'