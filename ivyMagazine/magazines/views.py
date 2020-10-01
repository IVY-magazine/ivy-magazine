from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    context = {}
    return render(request, 'magazines/homepage.html', context)

def magazine(request):
    context = {}
    return render(request, 'magazines/magazine.html', context)