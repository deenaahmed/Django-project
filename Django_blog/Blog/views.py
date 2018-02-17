from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import commentform
from django.http import HttpResponseRedirect
from django.template import RequestContext
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
#	messages.info(request,"geeet")
#	form= commentform()
#	print "get new_comment"
#	if request.method=="POST":
#		print "method b post"
#		form=commentform(request.POST)
#		if form.is_valid():
#			form.save()
#			return JsonResponse(serializers.serialize('json',Comment.objects.all()),safe=False)
	#return render(request, 'postpage.html')
	
	#return render(request, 'postpage.html',context1)


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




#def new_student(request):
#	form= stform()
#	if request.method=="POST":
#		form=stform(request.POST)
#		if form.is_valid():
#			form.save()
#			return HttpResponseRedirect('allstudent/')
#	return render(request,'new.html',{'form':form})

	

#def comment_delete(request,comment_id):
#	comm=comment.objects.get(id=comment_id)
#	comm.delete()	
#	return HttpResponseRedirect('allstudent/')	

#def reply_delete(request,comment_id):
#	comm=comment.objects.get(id=comment_id)
#	comm.delete()	
#	return HttpResponseRedirect('allstudent/')






