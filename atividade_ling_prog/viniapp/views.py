from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render(request, "viniapp/index.htm")

def redes_sociais(request):
    return render(request, "viniapp/redes_sociais.htm")

def musicas(request):
    return render(request, "viniapp/musicas.htm")