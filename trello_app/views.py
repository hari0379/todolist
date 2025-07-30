from django.shortcuts import render,redirect
from .models import TaskList,Task
from .forms import TaskForm,TaskForm_new
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html')
@login_required(login_url='login')
def create_new(request):
    if(request.method=='POST'):
        #fetch the data to the database
        list_name=request.POST['list_name']
        list=TaskList(name=list_name,user=request.user)
        list.save()
        return redirect('home')
    else:
         return render(request,'new_list.html')


@login_required(login_url='login')
def create_task(request):
    if(request.method=='POST'):
        #fetch the data to the database
        form=TaskForm_new(data=request.POST)
        form.save()
        return redirect('home')
    else:
        form=TaskForm_new()

        return render(request,'new_task.html',{'form':form})