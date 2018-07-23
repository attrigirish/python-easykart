from django.shortcuts import render,redirect
from main.models import Login
from django.http import HttpResponse

# Create your views here.
def login(request):
	if(request.method=='GET'):
		return render(request,'administrator/adminLogin.html',None)
	else:
		id=request.POST.get('loginid')
		Password=request.POST.get('password')
		try:
			u=Login.objects.get(email=id)
			if(u.password==Password):
				return HttpResponse('loged in successfully')#r=redirect('adminHome.html')return r
			else:
				msg='incorrect password'
				return render(request,'administrator/adminLogin.html',{'msg':msg})
		except:
			msg='incorrect username'
			return render(request,'administrator/adminLogin.html',{'msg':msg})



		