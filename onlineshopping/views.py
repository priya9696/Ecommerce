from django.shortcuts import render,redirect
from onlineshopping.forms import CategoryForm, Category,ProductForm, Product, User, UserForm
from . import forms
from onlineshopping.forms import feedback, feedbackForm
from.models import Cart, MyOrders
from django.db.models import F, Sum

def index(request):
    cl=Category.objects.all()
    pl=Product.objects.all()
    return render(request, 'index.html',{'cl':cl,'pl':pl})
   #cl side bar
   # pl main page


def home(request):
    return render(request, 'addUser.html')


def login(request):
    return render(request, 'login.html')


def loginpage(request):
   email=request.POST.get('email')
   passw=request.POST.get('passw') 
   if email=='admin' and passw=='admin':
       request.session['adminName']= email
       return redirect('/')                                                                                                                                                                                                                     
   try:
       ul=User.objects.get(email=email)
       if email==ul.email and passw==ul.password:
           request.session['userName']= email   #this lets your session to keep you logged in
           return redirect('/')
       else:
           return render(request, 'login.html',{'lmsg':"Invalid User Name and Password"})
    
   except:
       return render(request, 'login.html',{'lmsg':"Invalid User Name and Password"})


def Logoutbutton(request):
    ls=list(request.session.keys())
    for i in ls:
        del request.session[i]
    return redirect('/')

def addfeedback(request):
    f=feedbackForm
    return render(request,'addfeedback.html',{'form':f})

def feedb(request):
    f=feedbackForm(request.POST)
    f.save()
    return render(request,'index.html')

def addtocart(request):
    pid=request.GET.get('pid')
    print("pid", pid)
    prod=Product.objects.get(id=pid)
    email=request.session.get('userName')
    u=User.objects.get(email=email)
    cr=Cart()  #ct is an object of Class Cart()
    cr.pid=prod
    cr.email=u
    cr.save()
    return redirect('/')

def CartList(request):
    email=request.session.get('userName')
    crlist=Cart.objects.filter(email=email)
    cl=Category.objects.all()
    return render(request, 'CartList.html',{'crlist':crlist, 'cl':cl})
'''
def deleteItem(request):
    pid=request.GET.get('pid')
    print(pid)
    crlist=Cart.objects.filter(id=pid)
    crlist.delete()
    return render(request,'CartList.html',{'crlist':crlist})

'''
def addToMyOrder(request):
    pid=request.GET.get('pid')
    print("pid", pid)
    prod=Product.objects.get(id=pid)
    email=request.session.get('userName')
    u=User.objects.get(email=email)
    cr=Cart()  #ct is an object of Class Cart()
    cr.pid=prod
    cr.email=u
    cr.save()
    return redirect('/')

def myOrder(request):
    qt=request.session.get('qty')
    crlist=Cart.objects.filter(email=qt)
    email=request.session.get('userName')
    crlist=Cart.objects.filter(email=email)
    price=request.session.get('Price')
    prodd=Product.objects.filter(id=price)
    summ= MyOrders.objects.filter().aggregate(hello=(Sum(F('qty')*F('Price'))))
    order=MyOrders.objects.all()
    cl=Category.objects.all()
    return render(request, 'myOrder.html',{'sum':summ, 'crlist':crlist,'prodd': prodd,'order':order, 'cl':cl})

def search(request):
    return render(request, 'search.html')
'''
def SearcH(request):
    sr=request.POST.get('st')
    pl=Product.objects.filter(Pname__contains=sr)
    #pl=Product.objects.filter(Pname__startswith=sr)
    cl=Category.objects.all()
    return render(request, 'search.html', {'cl':cl, 'pl':pl})


to get all both the def in one 
def search(request):
    if method=="POST"
        sr=request.POST.get('st')
        pl=Product.objects.filter(Pname__contains=sr)
        cl=Category.objects.all()
        return render(request, 'index.html', {'cl':cl, 'pl':pl})
    else:
        return render(request, 'search.html', {'cl':cl, 'pl':pl})
'''



