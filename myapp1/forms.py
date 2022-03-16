from django import forms
from .models import *

class MyApp1Form(forms.ModelForm):
    class Meta:
            model = Stocks
            fields= "__all__"

    class Meta:
            model = Customer
            fields= "__all__"

class BookForm(forms.ModelForm):
         
    class Meta:
            model = Stocks
            fields= "__all__"

class AdminForm(forms.ModelForm):
         
    class Meta:
            model = Admin
            fields= "__all__"

class CustomerForm(forms.ModelForm):
         
    class Meta:
            model = Customer
            fields= ('Fname','Lname','ContactNum')



class LogInForm(forms.ModelForm):
         
    class Meta:
            model = Customer
            fields= ('Username','Password')