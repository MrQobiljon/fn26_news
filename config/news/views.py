from django.shortcuts import render

from .models import Category, Post

# Create your views here.


def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        'categories': categories,
        'posts': posts
    }

    return render(request, 'index.html', context)


def posts_by_category(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id)
    context = {
        "posts": posts,
        'categories': categories
    }
    return render(request, "index.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, 'detail.html', context)