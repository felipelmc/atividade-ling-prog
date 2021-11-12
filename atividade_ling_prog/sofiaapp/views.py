from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponse("<strong>SOFIA</strong>")

#def sofia(request):
    #return render(request,'sofiaapp/sofia-dtl.html')

#def laks(request):
    #return render(request, 'sofiaapp/laks.html')
  
#def vitz(request):
    #return render(request, 'sofiaapp/vitz.html')

def view_dinamica_int(request, param):
    if param == 0:
        return HttpResponse('<strong>Parâmetro 0</strong>')
    elif param == 1:
        return HttpResponse('<strong>Parâmetro 1</strong>')
    elif param == 2:
        return HttpResponse('<strong>Parâmetro 2</strong>')
    else:
        return HttpResponseNotFound('Página não existe!')

def view_dinamica_str(request, param):
    if param == 'sofia':
        return render(request, 'sofiaapp/sofia.html')
    elif param == 'laks':
        return render(request, 'sofiaapp/laks.html')
    elif param == 'vitz':
        return render(request, 'sofiaapp/vitz.html')
    else:
        return HttpResponseNotFound("Página não existe!")

def redireciona(request):
    url_redirecionamento = reverse('dinamica-str', args=['sofia'])
    return HttpResponseRedirect(url_redirecionamento)

def special_dtl(request):
    context = {
        'nome': 'Sofia',
        'nome_familia': 'Lakschevitz',
        'comida': 'açaí',
        'numero': [1,2,3,4],
    }
    return render(request, 'sofiaapp/aifos-dtl.html', context)