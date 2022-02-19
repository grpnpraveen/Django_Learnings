from operator import index
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"index.html",{"name":"praveen gali"})
def add(request):
    if(request.method=="GET"):
        result=int(request.GET['x'])+int(request.GET['y'])  # must be single quote
    if(request.method=="POST"):
        result=int(request.POST['x'])+int(request.POST['y'])  # must be single quote
    return render(request,"result.html",{"result":result})