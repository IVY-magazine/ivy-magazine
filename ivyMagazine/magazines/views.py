from django.shortcuts import render, redirect


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'magazines/register.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'magazines/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# Create your views here.
def home(request):
    context = {}
    return render(request, 'magazines/homepage.html', context)

def loginHome(request):
    context = {}
    return render(request, 'magazines/loginHome.html', context)

def blog(request):
    context = {}
    return render(request, 'magazines/blog.html', context)

@login_required(login_url = 'login')
def portfolio(request):
    context = {}
    return render(request, 'magazines/portfolio.html', context) 

@login_required(login_url = 'login')
def magazine(request):
    magazine = Magazine.objects.all()
    magazine = sorted(magazine,key = lambda x : x.date_created)
    return render(request, 'magazines/magazine.html', {'magazine':magazine})

def aboutUs(request):
    context = {}
    return render(request, 'magazines/aboutUs.html', context)

def contactUs(request):
    context = {}
    return render(request, 'magazines/contactUs.html', context)

@login_required(login_url = 'login')
def info(request):
    context = {}
    return render(request, 'magazines/info.html', context)

def signIn(request):
    context = {}
    return render(request, 'magazines/signIn.html', context)

def signUp(request):
    context = {}
    return render(request, 'magazines/signUp.html', context)