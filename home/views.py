from django.shortcuts import render

# Create your views here.

def index(request): 
    return render(request, 'home/index.html')

def contactus(request): 
    return render(request, 'home/contactus.html')

def privacy(request): 
    return render(request, 'home/privacy.html')

def sent(request): 
    return render(request, 'home/sent.html')

def shipping(request): 
    return render(request, 'home/shipping.html')