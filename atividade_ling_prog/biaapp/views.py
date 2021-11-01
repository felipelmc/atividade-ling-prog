from django.http import request
from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<strong>Bianca</strong>')

def bia(request):
    return render(request, 'biaapp/bia.html')

def pag1(request):
    return render(request, 'biaapp/pag1.html')

def pag2(request):
    return render(request, 'biaapp/pag2.html')