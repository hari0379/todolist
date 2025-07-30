from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from trello_app.models import Task,TaskList
def register(request):
    if request.method == 'POST' :
        #form=UserCreationForm(data = request.POST)
        form=CreateUserForm(data= request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CreateUserForm()
    return render(request,'pages/register.html',{'form':form})
@login_required(login_url='/login/')
def dashboard(request):
    user=request.user
    #lists=user.tasklist_set.all()
    lists=TaskList.objects.filter(user=user)
    tasks=Task.objects.filter(list__in=lists)
    return render(request,'pages/dashboard.html',{'lists':lists,'tasks':tasks})
def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'username or password is incorrect')
    return render(request,'pages/login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'pages/home.html')