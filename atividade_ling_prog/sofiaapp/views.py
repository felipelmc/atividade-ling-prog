from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>SOFIA</strong>")

def sofia(request):
    return render(request,'sofia.html')