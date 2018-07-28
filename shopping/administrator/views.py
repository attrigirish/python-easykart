from django.shortcuts import render,redirect
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

