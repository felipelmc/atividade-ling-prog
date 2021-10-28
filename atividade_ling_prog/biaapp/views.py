from django.http import request
from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<strong>Bianca</strong>')

def bia(request):
    return render(request, 'bia.html')