from django.shortcuts import render
from .models import cars,carsfromdatabaser
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
# Create your views here.
def TravelloHome(request):
    staticpath="static/images/"
    car1=cars()
    car1.name="Ull"
    car1.year="2034"
    car1.model="XrET"
    car1.cost=5243123
    car1.offer=False
    car1.img=staticpath+"car1.jpg"
    car2=cars()
    car2.name="fre"
    car2.year="989"
    car2.model="Rtx45"
    car2.cost=32355234
    car2.offer=True
    car2.img=staticpath+"car2.jpg"
    car3=cars()
    car3.name="eewd"
    car3.year="323"
    car3.offer=False
    car3.model="Dfe"
    car3.cost=232323
    car3.img=staticpath+"car3.jpg"
    webcars=[car1,car2,car3]
    return render(request,"travellohome.html",{"cars":webcars,"dataloadtype":"classObject","fromclass":True,"frompostgres":False})
def TravelloHomePostgres(request):
    if(request.user.is_authenticated):
        webcars=carsfromdatabaser.objects.all()
        return render(request,"travellohome.html",{"cars":webcars,"dataloadtype":"postgres","fromclass":False,"frompostgres":True})
    else:
        return render(request,"Error.html")