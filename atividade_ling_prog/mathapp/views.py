from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<strong>Teste do Matheus</strong>')

def matheus(request):
    return render(request, 'mathapp/matheus.html')

def matheus2(request):
    return render(request, 'mathapp/matheus2.html')

def matheus3(request):
    return render(request, 'mathapp/matheus3.html')