from django.shortcuts import render,redirect
<<<<<<< HEAD
from django.http import HttpResponse
from main.models import *
from main.forms import *


#Category Views

def AddCategory(request):
	if(request.method=='GET'):		
		form=CategoryForm()
		data={'form':form}
		return render(request,'administrator/addcategory.html',data)
	else:
		form=CategoryForm(request.POST)
		form.save()
		return redirect('/admin/categories/')
		
def DeleteCategory(request,id):
	category=Category.objects.get(id=id)
	category.delete()
	return redirect('/admin/categories/')


def UpdateCategory(request,id):
	if(request.method=='GET'):		
		category=Category.objects.get(id=id)
		formdata={'parentid':category.parentid,'name':category.name,'description':category.description}
		form=CategoryForm(formdata)
		data={'form':form}
		return render(request,'administrator/addcategory.html',data)
	else:
		category=Category.objects.get(id=id)
		form=CategoryForm(request.POST, instance=category)
		form.save()
		return redirect('/admin/categories/')

def Categories(request):
	categories=Category.objects.filter()
	data={'categories':categories}
	return render(request,'administrator/categories.html',data)

=======
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



		
>>>>>>> 69bcefa0db67ed8f6eb27f4965ba1566b6d6f5ee
