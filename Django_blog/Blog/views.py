from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def allPosts(request):
    all_posts = Post.objects.all()
    context = {"allPosts": all_posts}
    return render(request, "blog/home.html", context)
