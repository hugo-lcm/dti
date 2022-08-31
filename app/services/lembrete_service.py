# métodos para manipulação do banco de dados
from ..models import Lembrete


def cadastrar_lembrete(lembrete):
    Lembrete.objects.create(titulo=lembrete.titulo, descricao=lembrete.descricao,
                            data=lembrete.data, prioridade=lembrete.prioridade)


def listar_lembretes():
    # igual a select * from app_lembrete
    return Lembrete.objects.all()


def listar_lembrete_id(id):
    return Lembrete.objects.get(id=id)


# recebe o lembrete já inserido no bd e o novo
def editar_lembrete(lembrete_bd, novo_lembrete):
    lembrete_bd.titulo = novo_lembrete.titulo
    lembrete_bd.descricao = novo_lembrete.descricao
    lembrete_bd.data = novo_lembrete.data
    lembrete_bd.prioridade = novo_lembrete.prioridade
    lembrete_bd.save(force_update=True)


def excluir_lembrete(lembrete_bd):
    lembrete_bd.delete()