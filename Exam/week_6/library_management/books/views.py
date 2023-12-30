from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

def add_book(request):
    if request.method == 'POST': # user post request koreche
        book_form = forms.BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            print(book_form)
            return redirect('add_book')
    
    else: # user normally website e gele blank form pabe
        book_form = forms.BookForm()
    return render(request, 'add_book.html', {'form' : book_form})

class AddPostCreateView(CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('add_book')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)