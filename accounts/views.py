from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
# Create your views here.


def AccountsLogin(request):
    if request.method=="POST":
        uname=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(username=uname,password=pwd)
        if(user is not None):
            auth.login(request,user)
            print(user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
        return redirect('AccountsLogin')
    else:
        return render(request,"login.html")

def AccountsLogout(request):
    auth.logout(request)
    return redirect('/')
def AccountsRegister(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        uname=request.POST['username']
        email=request.POST['email'] 
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if(pass1==pass2):
            if User.objects.filter(username=uname).exists():
                messages.info(request,'user name taken')
                print('user name taken')
                return redirect('AccountsRegister')
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                print('email  taken')
                return redirect('AccountsRegister')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
                user.save()
                print('user created')
                return redirect('AccountsLogin')
        else:
            messages.info(request,'password not match')
            print("password not match")
            return redirect('AccountsRegister')  #need to pass function name
        return redirect('/')
    else:
        return render(request,"register.html")
