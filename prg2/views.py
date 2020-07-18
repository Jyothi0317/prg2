from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hello this is project2")

def home(request):
    return HttpResponse("<h1>home page of project2<h1>")

def html_demo1(request):
    return render(request,"sample.html")
