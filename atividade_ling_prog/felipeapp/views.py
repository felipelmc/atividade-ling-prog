from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
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
        raise Http404()
        # return HttpResponseNotFound("Página não existe!")
    
def view_dinamica_str(request, param):
    if param == 'redes-sociais':
        return render(request, 'felipeapp/redes-sociais.html')
    elif param == 'musicas':
        return render(request, 'felipeapp/musicas.html')
    elif param == 'faculdade':
        return render(request, 'felipeapp/faculdade.html')
    else:
        raise Http404()
        # return HttpResponseNotFound("Página não existe!")
    
def redireciona(request):
    url_redirecionamento = reverse('dinamica-str', args=['redes-sociais'])
    return HttpResponseRedirect(url_redirecionamento) 

def special_dtl(request):
    lista_de_cursos = ['ciência de dados', 'matemática aplicada']
    lista_de_signos = ['Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem', 'Libra', 'Scorpio',
                       'Sagitário', 'Capricórnio', 'Aquário', 'Peixes']
    
    context = {
        'nome':'Amiguinho',
        'nome_familia':'Lamarca',
        'cursos': lista_de_cursos,
        'signos': lista_de_signos
    }
    return render(request, 'felipeapp/felipeapp-dtl.html', context)