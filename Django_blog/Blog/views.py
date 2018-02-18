
from distutils.command import register
from django.contrib.sessions import serializers
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .forms import commentform
import re
from django.db.models import Q
from .models import *
from django.template import RequestContext



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

# Create your views here.

def filterwithoutbadwords(comment):
	commentsplitted=comment.split()
	ob2 = BadWord.objects.all() 
	counter=0
	for c in commentsplitted:
		c=c.lower()
		for o in ob2:
			o=o.name.lower()
			if c == o:
				size=len(c)
				cnew=""
				for cindex in c:
					cnew=cnew+"*"
					cnew=str(cnew)
				commentsplitted[counter]=cnew
		counter+=1
	mylists=""
	for uu in commentsplitted:
		mylists = mylists + uu
		mylist2=str(mylists)
	return mylist2

def postPage(request,post_id,user_id):
	form = commentform()
	ob = Post.objects.get(id=post_id)
	ob1 = Comment.objects.raw("select * from Blog_comment where post_id=post_id")
	xx=[]
	index=0
	for x in ob1:
		varg =filterwithoutbadwords(x.body)
		xx.append(varg)
		ob1[index].body=varg
		index +=1
	zipped_data= zip(ob1,xx)	
	#ob1.body=xx
	#
	ob2 = Reply.objects.all()  
	context = {'post_list':ob,
	'comment_list':ob1,
	'comment_body':xx,
	'zipped_data':zipped_data,
	'reply_list':ob2,
	}
	if request.method=="POST":
		#lcomment=Comment.objects.raw("select * from Blog_comment where post_id=post_id")
		varf=request.POST.get('body')
		vare=filterwithoutbadwords(varf)
		ob1= form.save(commit=False)
		ob1.user_id=user_id
		ob1.post_id=post_id
		ob1.body=varf
		#if ob1.is_valid():
		ob1.save()

	
	return render(request, 'postpage.html', context)

def new_comment(request,post_id,user_id):

	varf=request.POST.get('body')
	vare=filterwithoutbadwords(varf)
	ob1= form.save(commit=False)
	ob1.user_id=1
	ob1.post_id=1
	ob1.body=varf #hna lw 7nsave f l db bl * n5leha vare
	ob1.save()
	return JsonResponse(serializers.serialize('json',Comment.objects.all()),safe=False)



def comment_delete(request,comment_id,post_id,user_id):
	comm=Comment.objects.get(id=comment_id)
	comm.delete()	
	ob = Post.objects.get(id=post_id)
	ob1 = Comment.objects.raw("select * from Blog_comment where post_id=post_id")
	ob2 = Reply.objects.all()  
	context = {'post_list':ob,
	'comment_list':ob1,
	'reply_list':ob2,
	}
	return render(request, 'postpage.html', context)









def sub(request):

    catsub=Category.objects.filter(subscribe=request.user.id)
    cat_sub=[]
    for i in catsub:
        cat_sub.append(i.id)
    return cat_sub
