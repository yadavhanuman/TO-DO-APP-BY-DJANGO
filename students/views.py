from django.shortcuts import render,redirect
from .models import *
from .forms import *

def index(request):
    if request.method=="POST":
        a= todoForm(request.POST)
        if a.is_valid():
            a.save()
    a=todoForm()
    b=todo.objects.all()
    return render(request,'index.html',{'forms':a,"data":b})

def delete(request,id):
    c= todo.objects.get(id=id)
    c.delete()
    return redirect('index')




# Create your views here.
