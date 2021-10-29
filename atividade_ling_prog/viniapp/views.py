from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<strong> Vini aqui </strong>")

def vini(request):
    return render(request, "vini.htm")