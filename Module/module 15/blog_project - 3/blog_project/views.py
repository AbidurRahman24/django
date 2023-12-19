from django.shortcuts import render
from post.models import Post
from category.models import Category

def home(request, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None: # ekhn category slug jodi None na hoy tar mane sekhane value ache
        category = Category.objects.get(slug = category_slug) # slug je field model e likhechilam seta = amader category slug kore dilam taile ekhn kon category er slug sei category object peye jabo
        data = Post.objects.filter(category  = category) # post er category te category object bosiye filter korlam, ager data er sathe overright hoye jabe
    categories = Category.objects.all() # sob category dekhabo
    return render(request, 'home.html', {'data' : data, 'category' : categories})