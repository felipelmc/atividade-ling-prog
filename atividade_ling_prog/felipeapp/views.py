from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<strong>Teste do Felipe</strong>')

def pag1(request):
    return render(request, 'felipeapp/redes-sociais.html')

def pag2(request):
    return render(request, 'felipeapp/musicas.html')

def pag3(request):
    return render(request, 'felipeapp/faculdade.html')
