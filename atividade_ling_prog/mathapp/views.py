from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return HttpResponse('<strong>Teste do Matheus</strong>')

def matheus(request):
    return render(request, 'mathapp/matheus.html')

def matheus2(request):
    return render(request, 'mathapp/matheus2.html')

def matheus3(request):
    return render(request, 'mathapp/matheus3.html')

def redireciona(request):
    url_redirecionamento = reverse('dinamica_str', args=['leao'])
    return HttpResponseRedirect(url_redirecionamento)

def retorna_html(request):
    return render(request, 'mathapp/matheus3.html')

def view_dinamica_int(request, param):
    if pram == 0:
        return HttpResponse('<strong>Paraâmetro 0</strong>')
    elif param == 1:
        return HttpResponse('<strong>Paraâmetro 1</strong>')
    elif param == 2:
        return HttpResponse('<strong>Paraâmetro 2</strong>')
    else:
        return HttpResponseNotFound('Página não Encontrada')

def view_dinamica_str(request, param):
    if param == 'leao':
        return HttpResponse('<strong>Você se acha</strong>')
    else:
        return HttpResponseNotFound('Página não Encontrada')


def special_dtl(request):
    lista_de_cursos = ['ciência de dados', 'matemática aplicada']
    lista_de_signos = ['Peixes', 'Aquario', 'Leão', 'Cancer', 'Libra']
    context = {
       'pessoa':'Tio',
       'adjetivo':'Rafa',
       'cursos' : lista_de_cursos,
       'signos' : lista_de_signos
    }
    return render(request, 'mathapp/mathapp-dtl.html', context)