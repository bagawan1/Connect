from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def profile(request):
    current_user=request.user
    username=current_user.username
    email=current_user.email
    fname=current_user.first_name+" "+current_user.last_name
    context={'user':username,'mail':email,'name':fname}
    return render(request,'profile.html',context)
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        name=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('pass')

        new_user=User.objects.create_user(name, email, password)
        new_user.first_name=fname
        new_user.last_name=lname
        new_user.save()
        return redirect('login_view')
    return render(request,'register.html', {})


def login_view(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        password=request.POST.get('pass')

        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Error')
    return render(request, 'login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login_view')
def sports(request):
    return render(request, 'sports.html')
def national(request):
    return render(request, 'national_news.html')
def ent(request):
    return render(request, 'ent.html')
