from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<strong>Teste do Felipe</strong>')

def felipe(request):
    return render(request, 'felipeapp/felipe.html')


