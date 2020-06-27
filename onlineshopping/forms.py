from django import forms
from.models import Category
from.models import User
from.models import Product
from.models import feedback


class CategoryForm(forms.ModelForm):
    class Meta: 
        model=Category 
        fields = '__all__' 

class UserForm(forms.ModelForm):
    class Meta: 
        model=User 
        fields = '__all__' 
        widgets={'password':forms.PasswordInput}

class ProductForm(forms.ModelForm):
    class Meta: 
        model=Product 
        fields = '__all__' 
        
class feedbackForm(forms.ModelForm):
    class Meta: 
        model=feedback 
        fields = '__all__' 