from django.shortcuts import render
from Blog.models import *
# Create your views here.


def test(request):
    posts = Post.objects.all()
    return render(request, "all_posts.html", {"Posts": posts})