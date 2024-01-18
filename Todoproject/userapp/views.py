from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.app.models import user
from django.contrib import app

# Create your views here.
def registerUser(req):
    if req.method=='POST':
        fname=req.POST.get("fname","")
        lname=req.POST.get("lname","")
        email=req.POST.get("email","")
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        cpassword=req.POST.get("cpassword","")
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,"username already exist")
                return redirect('app:register')
            if User.objects.filter(email=email).exists():
                messages.info(req,"email already exist")
                return redirect('app:register')
            else:
                user=user.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                return redirect('home')
        else:
            messages.info(req,"password not matched")
            return redirect('app:register')    
            
                
    return render(req,'registeruser.html')        
