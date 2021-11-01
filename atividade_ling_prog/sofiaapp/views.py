from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>SOFIA</strong>")

def sofia(request):
    return render(request,'sofiaapp/sofia.html')

def laks(request):
    return render(request, 'sofiaapp/laks.html')