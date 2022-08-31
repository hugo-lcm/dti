from django.shortcuts import render, redirect
from .forms import LembreteForm
from .entidades.lembrete import Lembrete
from .services import lembrete_service


def listar_lembretes(request):
    lembretes = lembrete_service.listar_lembretes()
    return render(request, 'lembretes/listar_lembretes.html', {'lembretes': lembretes})


def cadastrar_lembrete(request):
    if request.method == 'POST':
        # se o método for == POST, vai passar os dados da requisição para o formulário
        form_lembrete = LembreteForm(request.POST)
        if form_lembrete.is_valid():
            # captura as infos que vierem do formulário
            titulo = form_lembrete.cleaned_data['titulo']
            descricao = form_lembrete.cleaned_data['descricao']
            data = form_lembrete.cleaned_data['data']
            prioridade = form_lembrete.cleaned_data['prioridade']
            novo_lembrete = Lembrete(titulo=titulo, descricao=descricao,
                                     data=data, prioridade=prioridade)
            # envia o objeto com os dados para o lembrete_service, que insere no BD
            lembrete_service.cadastrar_lembrete(novo_lembrete)
            return redirect('listar_lembretes')
    else:
        # cria uma instância vazia do formulário caso o método não seja POST
        form_lembrete = LembreteForm()
    return render(request, 'lembretes/form_lembrete.html', {'form_lembrete': form_lembrete})


def editar_lembrete(request, id):
    # armazena o lembrete que o usuário está buscando através do id
    lembrete_bd = lembrete_service.listar_lembrete_id(id)
    # retorna form vazio quando clicamos na opção de editar
    form_lembrete = LembreteForm(request.POST or None, instance=lembrete_bd)
    if form_lembrete.is_valid():
        titulo = form_lembrete.cleaned_data['titulo']
        descricao = form_lembrete.cleaned_data['descricao']
        data = form_lembrete.cleaned_data['data']
        prioridade = form_lembrete.cleaned_data['prioridade']
        novo_lembrete = Lembrete(titulo=titulo, descricao=descricao,
                                 data=data, prioridade=prioridade)
        lembrete_service.editar_lembrete(lembrete_bd, novo_lembrete)
        return redirect('listar_lembretes')

    return render(request, 'lembretes/form_lembrete.html', {'form_lembrete': form_lembrete})


def excluir_lembrete(request, id):
    lembrete_bd = lembrete_service.listar_lembrete_id(id)
    if request.method == 'POST':
        lembrete_service.excluir_lembrete(lembrete_bd)
        return redirect('listar_lembretes')
    return render(request, 'lembretes/confirmar_exclusao.html', {'lembrete': lembrete_bd})
