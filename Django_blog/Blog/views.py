from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import commentform
from django.http import HttpResponseRedirect
# Create your views here.


def postPage(request,post_id):
	ob = Post.objects.get(id=post_id)
	ob1 = Comment.objects.raw("select * from Blog_comment where post_id=post_id")
	ob2 = Reply.objects.all()  #7tb2a ashal lw 3ndna post id raw("select * from Blog_reply where post_id=post_id")
	context = {'post_list':ob,
	'comment_list':ob1,
	'reply_list':ob2,}
	
	return render(request, 'postpage.html', context)

#def new_comment(request,post_id,user_id):
#if request.method=="POST":
#		body = request.POST['commentbody']	
#		post = post_id
#		user = user_id
#		Comment.objects.create{
#		body=body,
#		post=post,
#		user=user,
#		}	
#		return HttpResponse('')
	

#def comment_delete(request,comment_id):
#	comm=comment.objects.get(id=comment_id)
#	comm.delete()	
#	return HttpResponseRedirect('allstudent/')	

#def reply_delete(request,comment_id):
#	comm=comment.objects.get(id=comment_id)
#	comm.delete()	
#	return HttpResponseRedirect('allstudent/')




