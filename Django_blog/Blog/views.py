
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from .models import Post,Like
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


def likePost(request):
        if request.method == 'GET':
               post_id = request.GET['post_id']
               likedpost = Post.objects.get(pk=post_id) #getting the liked posts
               likeObj = Like(post=likedpost) # Creating Like Object
               likeobj.state=1
               likeObj.save()  # saving it to store in database
               
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")

def dislikePost(request):
    counter=0
    if request.method == 'GET':
        post_id = request.GET['post_id']
        dislikedpost = Post.objects.get(pk=post_id) #getting the disliked posts
        dislikeObj = Like(post=dislikedpost) # Creating DisLike Object
        dislikeobj.state=0
        counter+=1
        if (counter>10):
            dislikedpost.delete()
        else:
             dislikeObj.save()  # saving it to store in database
             return HttpResponse("Success!") # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")









