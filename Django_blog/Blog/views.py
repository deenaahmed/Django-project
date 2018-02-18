from distutils.command import register
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from .models import *
import re

from django.db.models import Q


def allPosts(request):
    all_posts = Post.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(all_posts, 5)
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    all_cat = getCat()
    sub_cat = sub(request)
    context = {"allPosts": posts, "allCat": all_cat, "subcat": sub_cat}
    return render(request, "blog/home.html", context)


def search(request):

    try:
        tag = Tag.objects.get(name__icontains=request.GET['term'])
        byTag = Post.objects.filter(tag=tag.id).order_by('created_at')
    except Tag.DoesNotExist:
        byTag = None
    try:
        found_entries = Post.objects.filter(title__icontains=request.GET['term']).order_by('created_at')

    except Post.DoesNotExist:
        found_entries = None
    all_cat = getCat()
    sub_cat = sub(request)
    context = {"allPosts": found_entries, "tags": byTag, "allCat": all_cat, "subcat": sub_cat}
    return render(request, "blog/search.html", context)




def getCat():

    cat=Category.objects.all()
    return cat


def getPostsCat(request, cat_id):
    all_posts = Post.objects.filter(cat_id= cat_id).order_by('created_at')
    all_cat = getCat()
    sub_cat = sub(request)
    context = {"allPosts": all_posts, "allCat": all_cat, "subcat": sub_cat}
    return render(request, "blog/home.html", context)



def subscribe(request):
    cat_id = request.GET.get('catid', None)
    status = Category.subscribe.through.objects.filter(category_id=cat_id, user_id=request.user.id).exists()

    if status:
        #remove
        Category.subscribe.through.objects.filter(category_id=cat_id, user_id=request.user.id).delete()
        data = {
            'x': 1

        }

    else:
        Category.subscribe.through.objects.create(category_id=cat_id, user_id=request.user.id)

        data = {
            'x': 2

        }

    return JsonResponse(data)


def sub(request):

    catsub=Category.objects.filter(subscribe=request.user.id)
    cat_sub=[]
    for i in catsub:
        cat_sub.append(i.id)
    return cat_sub
