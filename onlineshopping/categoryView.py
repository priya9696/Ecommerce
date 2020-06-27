from django.shortcuts import render,redirect
from onlineshopping.forms import CategoryForm, Category, Product

def addCategoryPage(request):
    e=CategoryForm
    return render(request,'addCategoryPage.html',{'form':e})

def addCatPage(request):
    e=CategoryForm(request.POST)
    e.save()
    return render(request,'index.html')

def categoryList(request):
    cl=Category.objects.all()
    print(cl)
    return render(request,'categoryList.html',{'e':cl})

def deleteCategory(request):
    Cname=request.GET.get('Cname')
    #print(email)
    cl=Category.objects.get(Cname=Cname)
    cl.delete()
    return render(request,'index.html')


def categoryView(request):
    Cname=request.GET.get('Cname')
    pl=Product.objects.filter(Cname=Cname)
    cl=Category.objects.all()
    return render(request, 'index.html',{'cl':cl,'pl':pl})

    