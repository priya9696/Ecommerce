
from django.contrib import admin
from django.urls import path
from .import views
from .import categoryView
from .import userView
from .import productView

urlpatterns = [
    path('', views.index),
    path('home',views.home),
    path('addCategoryPage', categoryView.addCategoryPage),
    path('addCatPage', categoryView.addCatPage),
    path('userPage', userView.userPage),
    path('addUser', userView.addUser),
    path('addProductPage', productView.addProductPage),
    path('addProduct', productView.addProduct),
    path('categoryList', categoryView.categoryList),
    path('categoryView',categoryView.categoryView),
    path('userList', userView.userList),
    path('deleteUser', userView.deleteUser),
    path('editUser', userView.editUser),
    path('updateUser', userView.updateUser),
    path('productList', productView.productList),
    path('deleteproduct', productView.deleteproduct),
    path('editproduct', productView.editproduct),   
    path('updateProduct', productView.updateProduct),
    path('deleteCategory', categoryView.deleteCategory),
    path('login', views.login),
    path('loginpage', views.loginpage),
    path('Logoutbutton', views.Logoutbutton),
    path('addfeedback', views.addfeedback),
    path('feedb', views.feedb),
    path('addtocart', views.addtocart),
    path('CartList', views.CartList),
    path('search', views.search),
    #path('SearcH', views.SearcH),
    path('myOrder', views.myOrder),
    path('addToMyOrder', views.addToMyOrder),
   # path('deleteItem', views.deleteItem),

    

]
