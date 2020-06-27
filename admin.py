from django.contrib import admin
from onlineshopping.forms import CategoryForm, UserForm, ProductForm,  feedbackForm
from django.contrib.auth.models import Group
from django import forms
from.models import Category,User,Product, feedback, Cart, MyOrders


class ProductAdmin(admin.ModelAdmin):
    list_display=('id','Pname','Price','Description','Cname')
    list_filter=('id','Pname','Price','Description','Cname')



admin.site.site_header="shopping Site"




admin.site.register(Category)
admin.site.register(User)
admin.site.register(feedback)
admin.site.register(Cart)
admin.site.register(MyOrders)

admin.site.register(Product, ProductAdmin)
#admin.site.register(feedback, feedbackAdmin)

#admin.site.unregister(Group)   to remove Group or register