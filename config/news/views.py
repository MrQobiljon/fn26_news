from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Post

# Create your views here.


def index(request):
    # categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        # 'categories': categories,
        'posts': posts,
        "title": "Barcha yangiliklar!"
    }

    return render(request, 'index.html', context)


def posts_by_category(request, category_id):
    # categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category_id=category_id)
    context = {
        "posts": posts,
        # 'categories': categories,
        "title": f"{category.name}: Barcha maqolalar!"
    }
    return render(request, "index.html", context)


def post_detail(request: WSGIRequest, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post,
        "title": post.name
    }
    return render(request, 'detail.html', context)