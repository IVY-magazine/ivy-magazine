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
    magazines = Magazine.objects.all()
    return render(request, 'magazines/magazine.html', {'magazines': magazines})

def aboutUs(request):
    context = {}
    return render(request, 'magazines/aboutUs.html', context)

def contactUs(request):
    context = {}
    return render(request, 'magazines/contactUs.html', context)

def info(request):
    context = {}
    return render(request, 'magazines/info.html', context)

def signIn(request):
    context = {}
    return render(request, 'magazines/signIn.html', context)

def signUp(request):
    context = {}
    return render(request, 'magazines/signUp.html', context)