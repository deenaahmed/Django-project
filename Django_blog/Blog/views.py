from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import *
from .forms import commentform, RegistrationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Post, Like
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

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

def hello(request):
    data = request.GET['post_id']
    return HttpResponse(data)

def likePost(request,post_id,user_id):
    if request.method == 'GET':
        post_id = post_id
        likedpost = Post.objects.get(id=post_id)  # getting the liked posts
        like = Like(user_id= user_id, post=likedpost)  # Creating Like Object
        like.state = 1



        like.save()  # saving it to store in database

        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


def dislikePost(request):
    counter = 0
    if request.method == 'GET':
        post_id = request.GET['post_id']
        dislikedpost = Post.objects.get(pk=post_id)  # getting the disliked posts
        dislikeObj = Like(post=dislikedpost)  # Creating DisLike Object
        dislikeobj.state = 0
        counter += 1
        if (counter > 10):
            dislikedpost.delete()
        else:
            dislikeObj.save()  # saving it to store in database
            return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")


def filterwithoutbadwords(comment):
    commentsplitted = comment.split()
    ob2 = BadWord.objects.all()
    counter = 0
    for c in commentsplitted:
        c = c.lower()
        for o in ob2:
            o = o.name.lower()
            if c == o:
                size = len(c)
                cnew = ""
                for cindex in c:
                    cnew = cnew + "*"
                    cnew = str(cnew)
                commentsplitted[counter] = cnew
        counter += 1
    mylists = ""
    for uu in commentsplitted:
        mylists = mylists + uu
        mylist2 = str(mylists)
    return mylist2


def postPage(request, post_id, user_id):
    form = commentform()
    ob = Post.objects.get(id=post_id)
    ob1 = Comment.objects.raw("select * from Blog_comment where post_id=post_id")
    xx = []
    index = 0
    for x in ob1:
        varg = filterwithoutbadwords(x.body)
        xx.append(varg)
        ob1[index].body = varg
        index += 1
    zipped_data = zip(ob1, xx)
    # ob1.body=xx
    #
    ob2 = Reply.objects.all()
    context = {'post_list': ob,
               'comment_list': ob1,
               'comment_body': xx,
               'zipped_data': zipped_data,
               'reply_list': ob2,
               }
    if request.method == "POST":
        # lcomment=Comment.objects.raw("select * from Blog_comment where post_id=post_id")
        varf = request.POST.get('body')
        vare = filterwithoutbadwords(varf)
        ob1 = form.save(commit=False)
        ob1.user_id = user_id
        ob1.post_id = post_id
        ob1.body = varf
        # if ob1.is_valid():
        ob1.save()

    return render(request, 'postpage.html', context)


def new_comment(request, post_id, user_id):
    varf = request.POST.get('body')
    vare = filterwithoutbadwords(varf)
    ob1 = form.save(commit=False)
    ob1.user_id = 1
    ob1.post_id = 1
    ob1.body = varf  # hna lw 7nsave f l db bl * n5leha vare
    ob1.save()
    return JsonResponse(serializers.serialize('json', Comment.objects.all()), safe=False)


#	messages.info(request,"geeet")
#	form= commentform()
#	print "get new_comment"
#	if request.method=="POST":
#		print "method b post"
#		form=commentform(request.POST)
#		if form.is_valid():
#			form.save()
#			return JsonResponse(serializers.serialize('json',Comment.objects.all()),safe=False)
# return render(request, 'postpage.html')

# return render(request, 'postpage.html',context1)


def comment_delete(request, comment_id, post_id, user_id):
    comm = Comment.objects.get(id=comment_id)
    comm.delete()
    ob = Post.objects.get(id=post_id)
    ob1 = Comment.objects.raw("select * from Blog_comment where post_id=post_id")
    ob2 = Reply.objects.all()
    context = {'post_list': ob,
               'comment_list': ob1,
               'reply_list': ob2,
               }
    return render(request, 'postpage.html', context)


# def new_student(request):
#	form= stform()
#	if request.method=="POST":
#		form=stform(request.POST)
#		if form.is_valid():
#			form.save()
#			return HttpResponseRedirect('allstudent/')
#	return render(request,'new.html',{'form':form})


# def comment_delete(request,comment_id):
#	comm=comment.objects.get(id=comment_id)
#	comm.delete()	
#	return HttpResponseRedirect('allstudent/')	

# def reply_delete(request,comment_id):
#	comm=comment.objects.get(id=comment_id)
#	comm.delete()	
#	return HttpResponseRedirect('allstudent/')


# from loginApp.forms import RegistrationForm

# Create your views here.
def register(request):
    usr_form = RegistrationForm()
    if request.method == "POST":
        users = User.objects.all().filter(email=request.POST['email'])
        if users.exists():
            return render(request, "registration/register.html", {"form": usr_form, "this dublicated email": True})
        usr_form = RegistrationForm(request.POST)
        if usr_form.is_valid():
            usr_form.save()
            return HttpResponseRedirect("registeration/main_page")
    return render(request, "registration/register.html", {"form": usr_form})


def login_form(request):
    if request.method == 'POST':

        name = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=name, password=password)

        if user is not None:  # this means we found the user in database
            login(request, user)  # this means we put the user id in the session
            if user.is_active:
                login(request, user)
                return HttpResponse(' you are logged in succes')
            else:
                return HttpResponse('you are not active user')
        else:
            return HttpResponse('logged in not succes')


    else:
        return render(request, 'registration/login_form.html')

@login_required
def logged_in_only(request):
    return HttpResponse('you are authenticated')
