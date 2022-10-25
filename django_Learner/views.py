from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_Learner.apps import apiCall

from django_Learner.forms import StudentForm
from .models import Info
from django import forms

# Create your views here.
# it handles the request and returns the response
#in some it is also known as action

def hello(request):
    obj=Info.objects.all()
    text=apiCall()

    print(text)

    return render(request,"index.html",{'obj':obj,'text':text[0],'text2':text[1]})

# def addS(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         age=request.POST['age']
#         email=request.POST['email']
#         obj=Info(name=name,age=age,email=email)
#         obj.save()
#         return HttpResponse("Data Saved Successfully")
#     return render(request,"addStudent.html")

def addS(request):
    form=StudentForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        obj=Info.objects.all()
        content={'msg':"Data Saved Successfully",'obj':obj}
        return HttpResponse('New Student Was Added')

    context={'form':form}
    # if request.method=="POST":
    #     name=request.POST['name']
    #     age=request.POST['age']
    #     email=request.POST['email']
    #     obj=Info(name=name,age=age,email=email)
    #     obj.save()
    #    

    return render(request,"addStudent.html",context)


def update(request,id):
    obj=Info.objects.get(id=id)
    form=StudentForm(request.POST or None,instance=obj)
    context={'form':form}
    if form.is_valid():
        form.save()

        return HttpResponse("Data Updated Successfully")
    return render(request,"update.html",context)

def delete(request,id):

    obj=Info.objects.get(id=id)
    obj.delete()
    return HttpResponse("Data Deleted Successfully")