from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<strong>Teste do Pedro</strong>')

def pedro(request):
    return render(request, 'pedroapp/pedro.html')

def teste(request):
    return render(request, 'pedroapp/teste.html')