from django.shortcuts import render


def listar_lembretes(request):
    return render(request, 'lembretes/listar_lembretes.html')
