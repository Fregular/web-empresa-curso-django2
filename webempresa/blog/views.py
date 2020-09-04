from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request,'blog/blog.html',{'posts': posts})

def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)
    #posts = Post.objects.filter(categories=category)

    #return render(request, 'blog/category.html',{'category':category,
    #                                            'posts':posts})
    return render(request, 'blog/category.html', {'category': category})

'''
en category.html, si se cambia el {% for post in Post %}
por {% for post in category.post_set.all %} se busca las relaciones que tiene
category con post y las traera todas. Es posible tambien en cambiar el category.post_set.all por
"category.get_posts.all" agregando un parametros en models.py para "category" 'related_name="get_posts"'
'''