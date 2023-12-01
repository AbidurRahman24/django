from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'nav/about.html')

def contact(request):
    return render(request, 'nav/contact.html')
