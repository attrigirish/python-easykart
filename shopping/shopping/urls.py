"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

#Importing Views
from main import views as main
from seller import views as seller
from buyer import views as buyer
from administrator import views as administrator

urlpatterns = [

<<<<<<< HEAD
	#Category Model
	path('admin/category/add/', administrator.AddCategory),
	path('admin/category/delete/<int:id>/', administrator.DeleteCategory),
	path('admin/category/update/<int:id>/', administrator.UpdateCategory),
	path('admin/categories/', administrator.Categories),
=======
path('loginHome/',administrator.login),
>>>>>>> 69bcefa0db67ed8f6eb27f4965ba1566b6d6f5ee
]

urlpatterns += static("/",document_root=settings.BASE_DIR)
