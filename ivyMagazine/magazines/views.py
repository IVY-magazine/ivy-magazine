from django.shortcuts import render, redirect

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

def portfolio(request):
    context = {}
    return render(request, 'magazines/portfolio.html', context) 

def magazine(request):
    context = {}
    return render(request, 'magazines/magazine.html', context)

def aboutUs(request):
    context = {}
    return render(request, 'magazines/aboutUs.html', context)

def contactUs(request):
    context = {}
    return render(request, 'magazines/contactUs.html', context)

def info(request):
    context = {}
    return render(request, 'magazines/info.html', context)

   