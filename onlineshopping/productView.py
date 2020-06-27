from django.shortcuts import render,redirect
from onlineshopping.forms import ProductForm
from .models import Product

def addProductPage(request):
    p=ProductForm
    return render(request,'addproductPage.html',{'form':p})

def addProduct(request):
    p=ProductForm(request.POST)
    p.save()
    return render(request,'index.html')

def productList(request):
    pl=Product.objects.all()
    return render(request,'productList.html',{'p':pl})

def deleteproduct(request):
    id=request.GET.get('id')
    #print(id)
    pl=Product.objects.filter(id=id).first()
    pl.delete()
    return render(request,'index.html')

def editproduct(request):
    id=request.GET.get('id')
    pl=Product.objects.filter(id=id).first()
    p=ProductForm(instance=pl)
    return render(request,'editproduct.html',{'form':p, 'id':id})

def updateProduct(request):
    id=request.GET.get('id')
    pl=Product.objects.filter(id=id).first()
    p=ProductForm(request.POST,instance=pl)
    p.save()
    return redirect('/productList')


