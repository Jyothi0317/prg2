from django.http import HttpResponse

def index(request):
    return HttpResponse("hello this is project2")

def home(request):
    return HttpResponse("<h1>home page of project2<h1>")
