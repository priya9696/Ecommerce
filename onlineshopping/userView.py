from django.shortcuts import render,redirect
from onlineshopping.forms import UserForm, User


def userPage(request):
    u=UserForm
    return render(request,'userPage.html',{'form':u})

def addUser(request):
    u=UserForm(request.POST)
    u.save()
    return render(request,'index.html')

def userList(request):
    ul=User.objects.all()
    return render(request,'userList.html',{'u':ul})

def deleteUser(request):
    email=request.GET.get('email')
    #print(email)
    ul=User.objects.filter(email=email).first()
    ul.delete()
    return render(request,'index.html')


def editUser(request):
    email=request.GET.get('email')
    ul=User.objects.filter(email=email).first()
   
    u=UserForm(instance=ul)
    return render(request,'editUser.html',{'form':u, 'email':email})

def updateUser(request):
    email=request.GET.get('email')
    print("My Email ",email)
    ul=User.objects.filter(email=email).first()
    print("Mera Data",ul)
    u=UserForm(request.POST,instance=ul)
    u.save()
    return redirect('/userList')



