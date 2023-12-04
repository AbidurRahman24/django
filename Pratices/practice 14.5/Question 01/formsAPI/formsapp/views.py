from django.shortcuts import render
from . forms import contactForm
# Create your views here.
def show(request):
    return render(request, 'show.html')



#View Function for contactForm Form-Class
def DjangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'home.html', {'form':form})

    # if request.method == 'POST':
    #     form = contactForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         file = form.cleaned_data['file']
    #         with open('./formsapp/uploads/' + file.name, 'wb+') as destination:
    #             for chunk in file.chunks():
    #                 destination.write(chunk)
    #         print(form.cleaned_data)
    # else:
    #     form = contactForm()
    # return render(request, 'home.html', {'form':form}) 


