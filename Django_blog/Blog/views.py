from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import commentform,replyform
from django.http import HttpResponseRedirect, JsonResponse
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
	form1=replyform()
	ob = Post.objects.get(id=post_id)
	obb = Tag.objects.all()
	ob1 = Comment.objects.raw("select * from Blog_comment where post_id=post_id")
	xx=[]
	xx1=[]
	for x in ob1:
		varg =filterwithoutbadwords(x.body)
		xx.append(varg)
		ob5 = User.objects.get(id=x.user_id)
		xx1.append(ob5)
	zipped_data= zip(ob1,xx,xx1)	
	xx1=[]
	xx11=[]
	ob2 = Reply.objects.all()  
	for x1 in ob2:
		varg =filterwithoutbadwords(x1.body)
		xx1.append(varg)
		ob5 = User.objects.get(id=x1.user_id)
		xx11.append(ob5)
	zipped_data1= zip(ob2,xx1,xx11)
	context = {'post_list':ob,
	'tag_list':obb,
	'comment_list':ob1,
	'comment_body':xx,
	'zipped_data':zipped_data,
	'zipped_data1':zipped_data1,
	}
	#if request.method=="POST":
	#	varf=request.POST.get('body')
	#	vare=filterwithoutbadwords(varf)
	#	ob1= form.save(commit=False)
	#	ob1.user_id=user_id
	#	ob1.post_id=post_id
	#	ob1.body=varf
	#	ob1.save()

	
	return render(request, 'postpage.html', context)

def new_comment(request):
	form = commentform()
	ob1= form.save(commit=False)
	ob1.post_id=request.GET.get('post_id',None)
	ob1.user_id=1
	ob1.body=request.GET.get('body',None)
	ob1.save()
	username_calculated = User.objects.get(id=ob1.user_id)
	data = {
	'idd' :ob1.id,
	'username':ob1.user_id,
	'createdat':ob1.created_at
	}
	
	return JsonResponse(data)

def new_reply(request):
	form1 = replyform()
	ob1= form1.save(commit=False)
	ob1.comment_id=request.GET.get('comment_id_reply',None)
	#print ob1.comment_id
	ob1.user_id=1
	ob1.body=request.GET.get('bodyreply',None)
	#print ob1.body
	ob1.save()
	data = {
	'idd' :ob1.id,
	'username':ob1.user_id,
	'createdat':ob1.created_at 
	}
	return JsonResponse(data)



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


def comment_delete(request):
	comment_id=request.GET.get('comment_id',None)
	comm=Comment.objects.get(id=comment_id)
	comm.delete()
	data = {
	'x' :1
	}
	
	return JsonResponse(data)




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






