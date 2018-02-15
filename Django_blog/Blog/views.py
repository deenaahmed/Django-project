from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from .models import Post
import re

from django.db.models import Q


def allPosts(request):
    all_posts = Post.objects.all()
    context = {"allPosts": all_posts}
    return render(request, "blog/home.html", context)


def search(request):

    found_entries = Post.objects.filter(title__icontains=request.GET['term']).order_by('created_at')
    context = {"allPosts": found_entries}
    return render(request, "blog/home.html", context)









