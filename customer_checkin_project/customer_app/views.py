from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import *
from .models import *
import winsound 
def alarmsound(request):
    # Set frequency to 2000 Hertz
    frequency = 2000
    duration = 3000
    winsound.Beep(frequency, duration)
    return render(request,'landing.html')
    
# Create your views here.
def landingview(request):
	return render(request,'landing.html')

def loginview(request):
	form=LoginForm(request.POST or None)
	msg='no'
	if request.method== "POST":
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username, password=password )
			login(request,user)
		else:
			msg="Error validating form"

	return render(request,'login.html', {'form':form,'msg':msg})


def signoutview(request):
    #signout doesnt require a template
    logout(request)
    messages.success(request,"You are Logged out successfully")
    return redirect('landing')

def signupview(request):
    msg=None
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
        	user=form.save()
        	msg="User Created successfully"
        	return redirect('attendants')
        else:
        	msg="Form is not valid" 
    else:
    	form=SignupForm()
    return render(request,'signup.html',{'form':form, 'msg':msg})
