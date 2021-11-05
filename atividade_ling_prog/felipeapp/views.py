from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 

def index(request):
    return HttpResponse('<strong>Teste do Felipe</strong>')

#def pag1(request):
    #return render(request, 'felipeapp/redes-sociais.html')

# def pag2(request):
    # return render(request, 'felipeapp/musicas.html')

# def pag3(request):
    # return render(request, 'felipeapp/faculdade.html')

def view_dinamica_int(request, param):
    if param == 1:
        return HttpResponse('<strong>Parâmetro 1</strong>')
    elif param == 2:
        return HttpResponse('<strong>Parâmetro 2</strong>')
    elif param == 3:
        return HttpResponse('<strong>Parâmetro 3</strong>')
    else:
        return HttpResponseNotFound("Página não existe!")
    
def view_dinamica_str(request, param):
    if param == 'redes-sociais':
        return render(request, 'felipeapp/redes-sociais.html')
    elif param == 'musicas':
        return render(request, 'felipeapp/musicas.html')
    elif param == 'faculdade':
        return render(request, 'felipeapp/faculdade.html')
    else:
        return HttpResponseNotFound("Página não existe!")
    
def redireciona(request):
    url_redirecionamento = reverse('dinamica-str', args=['redes-sociais'])
    return HttpResponseRedirect(url_redirecionamento) 

def special_dtl(request):
    context = {
        'nome':'Amiguinho',
        'nome_familia':'Lamarca'
    }
    return render(request, 'felipeapp/felipeapp-dtl.html', context)