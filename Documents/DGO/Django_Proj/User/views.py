from django.shortcuts import render,redirect,HttpResponse
#from django.contrib.auth.forms import UserCreationForrm
from django.contrib import messages
from .forms import UserRegiserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
def register(request):
    if(request.method=="POST"):
        form=UserRegiserForm(request.POST)
        if(form.is_valid()):
                form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,f'Account Created for {username} now Login Plzzz ')
                return redirect('login')
                #return HttpResponse("<h1>Hello GYZZZZ</h1>")
        else:
            messages.warning(request,'Plzz check the validations Mr. Jo Bhi ho aap!!')
            form=UserRegiserForm()
            return render(request,'users/register.html',{'form':form})
    form=UserRegiserForm()
    return render(request,'users/register.html',{'form':form})  


def loginn(request):
    if(request.method=="POST"):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if(user):
                login(request,user)
                messages.success(request,f"Welcome {user.username}")
                return redirect('blog-home')
            else:
                messages.error(request,f"sorry there is no one with this {username}")      
    form=AuthenticationForm()      
    return render(request,'users/login.html',{'form':form})
        
@login_required
def logoutt(request):
    logout(request)        

@login_required
def profile(request):
    return render(request,"users/profile.html")