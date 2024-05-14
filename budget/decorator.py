from django.shortcuts import redirect
from django.contrib import messages

def my_decorator(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@my_decorator
def sub(n1,n2):
    return n1-n2

@my_decorator
def div(n1,n2):
    return n1/n2

print(sub(10,5))
print(div(10,20))

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper



