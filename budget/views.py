from django.shortcuts import render,redirect
from django.views.generic import View
from budget.forms import TransactionForm,RegistrationForm,LoginForm
from budget.models import Transaction
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils import timezone
from django.db.models import Sum,Count
from budget.decorator import signin_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.cache import never_cache


# Create your views here.


# url: localhost:8000/budget/transactions/add/
# method-post,get

@method_decorator([signin_required,never_cache],name="dispatch")
class TransactionCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TransactionForm()
        return render(request,"transaction_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=TransactionForm(request.POST)
        if form.is_valid():
            form.instance.user_object=request.user
            form.save()
            messages.success(request,"transaction added successfully")
            return redirect("transaction-list")
        messages.error(request,"failed to add")
        return render(request,"transaction_add.html",{"form":form})

# url:localhost:8000/budget/transactions/all/
# method:get
    
@method_decorator([signin_required,never_cache],name="dispatch")
class TransactionListview(View):
    def get(self,request,*args,**kwargs):
        # if not request.user.is_authenticated:
        #     return redirect("signin")
        qs=Transaction.objects.filter(user_object=request.user)
        cur_month=timezone.now().month
        cur_year=timezone.now().year
        group_by_qs=Transaction.objects.filter(
            user_object=request.user,
            created_date__month=cur_month,
            created_date__year=cur_year,
            ).values("type").annotate(type_sum=Sum("amount"),type_count=Count("type"))
        print(group_by_qs)
        group_by_category_qs=Transaction.objects.filter(
            user_object=request.user,
            created_date__month=cur_month,
            created_date__year=cur_year
        ).values("category").annotate(cat_sum=Sum("amount"),cat_count=Count("category"))
        print(group_by_category_qs)
        return render(request,"transaction_list.html",{"data":qs,"type_total":group_by_qs,"category_total":group_by_category_qs})
    

# url:localhost:8000/budget/transactions/{id}/change/
# method:get,post

@method_decorator([signin_required,never_cache],name="dispatch")
class TransactionUpdateView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        transaction_object=Transaction.objects.get(id=id)
        form=TransactionForm(instance=transaction_object)
        return render(request,"transaction_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        transaction_object=Transaction.objects.get(id=id)
        form=TransactionForm(request.POST,instance=transaction_object)
        if form.is_valid():
            form.save()
            messages.success(request,"transaction updated successfully")
            return redirect("transaction-list")
        messages.error(request,"failed to update")
        return render(request,"transaction_edit.html",{"form":form})
    

# url:localhost:8000/budget/transactions/{id}/remove/
# method=get

@method_decorator([signin_required,never_cache],name="dispatch")   
class TransactionDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Transaction.objects.get(id=id).delete()
        messages.success(request,"deleted successfuly")
        return redirect("transaction-list")
    
# url:localhost:8000/budget/transactions/{id}/
# method=get

@method_decorator([signin_required,never_cache],name="dispatch")
class TransactionDetailview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Transaction.objects.get(id=id)
        return render(request,"transaction_detail.html",{"data":qs})
    

# url-localhost:8000/budget/register/
# method-get,post
    
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # User.objects.create_user(**form.cleaned_data)
            # print("successful")
            form.save()
            
            return redirect('signin')
        return render(request,"register.html",{"form":form})
    

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                messages.success(request,"login success")
                return redirect("transaction-list")
        return render(request,"login.html",{"form":form})

@method_decorator([signin_required,never_cache],name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    


        
            

