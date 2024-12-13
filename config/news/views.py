from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Post
from .forms import PostForm

# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        "title": "Barcha yangiliklar!"
    }

    return render(request, 'index.html', context)


def posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category_id=category_id)
    context = {
        "posts": posts,
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


def add_post(request: WSGIRequest):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.create()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
    context = {
        "form": form
    }
    return render(request, 'add_post.html', context)