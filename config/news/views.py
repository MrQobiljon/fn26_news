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

    post.views += 1
    post.save()

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


def update_post(request: WSGIRequest, pk: int):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post.name = form.cleaned_data.get("name")
            post.content = form.cleaned_data.get("content")
            post.photo = form.cleaned_data.get("photo") if form.cleaned_data.get("photo") else post.photo
            post.category = form.cleaned_data.get("category")
            post.published = form.cleaned_data.get("published")
            post.video = form.cleaned_data.get("video") if form.cleaned_data.get("video") else post.video
            post.save()
            return redirect('detail', pk=post.pk)

    form = PostForm(initial={
        "name": post.name,
        "content": post.content,
        "photo": post.photo,
        "category": post.category,
        "published": post.published
    })

    context = {
        "form": form,
        'post': post
    }

    return render(request, 'add_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {
        "post": post
    }
    return render(request, 'confirm_delete.html', context)

