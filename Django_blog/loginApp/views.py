
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
from django.contrib.auth import authenticate,login


#from loginApp.forms import RegistrationForm

# Create your views here.
def register(request):
    usr_form=RegistrationForm()
    if request.method=="POST":
        users = User.objects.all().filter(email=request.POST['email'])
        if users.exists():
            return render(request, "registration/register.html", {"form": usr_form, "this dublicated email": True })
        usr_form = RegistrationForm(request.POST)
        if usr_form.is_valid():
            usr_form.save()
            return HttpResponseRedirect("registeration/main_page")
    return render(request, "registration/register.html",{"form":usr_form})

def login_form(request):

    if request.method == 'POST':

        name = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=name,password=password)

        if user is not None: #this means we found the user in database
            login(request,user)#this means we put the user id in the session

            return HttpResponse('logged in succes')
        else:
            return HttpResponse('logged in not succes')
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse(' you are logged in succes')
            else:
                return HttpResponse('you are not active user') 
        else:
            return render(request,'registration/login_form.html')


         

    return render(request,'registration/login_form.html')

#this is a decorator
#https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
@login_required
def logged_in_only(request):
    return HttpResponse('you are authenticated')









    