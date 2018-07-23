from django.shortcuts import render
from django.http import HttpResponse
from main.forms import *

# Create your views here.

def user_login(request):
	form=Loginform()
	#users=Login.objects.values()
	return render(request,"login.html",{'form':form})

def home(request):
	return render(request,"home.html",None)
