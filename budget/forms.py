from django import forms
from budget.models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        # fields="__all__"
        exclude=("created_date","user_object",)
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "type":forms.Select(attrs={"class":"form-control"}),
            "category":forms.Select(attrs={"class":"form-control"}),
            "amount":forms.NumberInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"})
        }

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))   #pass1 and pass2 are not from models, they are from UserCreationform, hence styling is different for them.
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))  
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))