from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<strong>Teste do Matheus</strong>')

def matheus(request):
    return render(request, 'matheus.html')