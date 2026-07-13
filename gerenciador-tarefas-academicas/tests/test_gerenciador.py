import pytest
from src.gerenciador import GerenciadorTarefas


def test_criar_tarefa_com_dados_validos():
    gerenciador = GerenciadorTarefas()

    id_tarefa = gerenciador.criar_tarefa(
        "Estudar pytest",
        "Engenharia de Software",
        "Revisar testes unitários",
        "alta",
        "2026-03-25"
    )

    assert id_tarefa == 1
    assert gerenciador.tarefas[1]["titulo"] == "Estudar pytest"
    assert gerenciador.tarefas[1]["status"] == "pendente"


def test_criar_duas_tarefas_gera_ids_diferentes():
    gerenciador = GerenciadorTarefas()

    id1 = gerenciador.criar_tarefa("Tarefa 1", "C14", "Desc 1", "baixa", "2026-03-25")
    id2 = gerenciador.criar_tarefa("Tarefa 2", "C14", "Desc 2", "media", "2026-03-26")

    assert id1 == 1
    assert id2 == 2


def test_buscar_tarefa_existente():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Estudar", "C14", "Descrição", "alta", "2026-03-25")

    tarefa = gerenciador.buscar_tarefa(id_tarefa)

    assert tarefa["titulo"] == "Estudar"
    assert tarefa["disciplina"] == "C14"


def test_listar_tarefas_retorna_dicionario_com_tarefas():
    gerenciador = GerenciadorTarefas()
    gerenciador.criar_tarefa("Tarefa A", "C14", "Desc", "alta", "2026-03-25")
    gerenciador.criar_tarefa("Tarefa B", "C15", "Desc", "media", "2026-03-26")

    tarefas = gerenciador.listar_tarefas()

    assert len(tarefas) == 2
    assert 1 in tarefas
    assert 2 in tarefas


def test_editar_tarefa_existente():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Antigo", "C14", "Desc", "baixa", "2026-03-25")

    gerenciador.editar_tarefa(id_tarefa, titulo="Novo título", prioridade="alta")

    tarefa = gerenciador.buscar_tarefa(id_tarefa)
    assert tarefa["titulo"] == "Novo título"
    assert tarefa["prioridade"] == "alta"


def test_remover_tarefa_existente():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Remover", "C14", "Desc", "media", "2026-03-25")

    gerenciador.remover_tarefa(id_tarefa)

    assert id_tarefa not in gerenciador.tarefas


def test_concluir_tarefa_existente():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Concluir", "C14", "Desc", "alta", "2026-03-25")

    gerenciador.concluir_tarefa(id_tarefa)

    assert gerenciador.tarefas[id_tarefa]["status"] == "concluida"


def test_filtrar_por_disciplina_retorna_apenas_tarefas_da_disciplina():
    gerenciador = GerenciadorTarefas()
    gerenciador.criar_tarefa("Tarefa 1", "C14", "Desc", "alta", "2026-03-25")
    gerenciador.criar_tarefa("Tarefa 2", "C15", "Desc", "media", "2026-03-26")
    gerenciador.criar_tarefa("Tarefa 3", "C14", "Desc", "baixa", "2026-03-27")

    resultado = gerenciador.filtrar_por_disciplina("C14")

    assert len(resultado) == 2
    assert all(tarefa["disciplina"] == "C14" for tarefa in resultado.values())


def test_filtrar_por_prioridade_retorna_apenas_tarefas_da_prioridade():
    gerenciador = GerenciadorTarefas()
    gerenciador.criar_tarefa("Tarefa 1", "C14", "Desc", "alta", "2026-03-25")
    gerenciador.criar_tarefa("Tarefa 2", "C15", "Desc", "media", "2026-03-26")
    gerenciador.criar_tarefa("Tarefa 3", "C16", "Desc", "alta", "2026-03-27")

    resultado = gerenciador.filtrar_por_prioridade("alta")

    assert len(resultado) == 2
    assert all(tarefa["prioridade"] == "alta" for tarefa in resultado.values())


def test_filtrar_por_status_retorna_apenas_tarefas_com_status_informado():
    gerenciador = GerenciadorTarefas()
    id1 = gerenciador.criar_tarefa("Tarefa 1", "C14", "Desc", "alta", "2026-03-25")
    gerenciador.criar_tarefa("Tarefa 2", "C15", "Desc", "media", "2026-03-26")

    gerenciador.concluir_tarefa(id1)

    resultado = gerenciador.filtrar_por_status("concluida")

    assert len(resultado) == 1
    assert resultado[id1]["status"] == "concluida"


def test_criar_tarefa_com_titulo_vazio_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Título não pode ser vazio"):
        gerenciador.criar_tarefa("", "C14", "Desc", "alta", "2026-03-25")


def test_criar_tarefa_com_disciplina_vazia_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Disciplina não pode ser vazia"):
        gerenciador.criar_tarefa("Tarefa", "", "Desc", "alta", "2026-03-25")


def test_criar_tarefa_com_prioridade_invalida_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Prioridade inválida"):
        gerenciador.criar_tarefa("Tarefa", "C14", "Desc", "urgente", "2026-03-25")


def test_buscar_tarefa_inexistente_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Tarefa não encontrada"):
        gerenciador.buscar_tarefa(999)


def test_editar_tarefa_inexistente_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Tarefa não encontrada"):
        gerenciador.editar_tarefa(999, titulo="Novo título")


def test_editar_tarefa_com_titulo_vazio_lanca_erro():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Tarefa", "C14", "Desc", "alta", "2026-03-25")

    with pytest.raises(ValueError, match="Título não pode ser vazio"):
        gerenciador.editar_tarefa(id_tarefa, titulo="")


def test_editar_tarefa_com_disciplina_vazia_lanca_erro():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Tarefa", "C14", "Desc", "alta", "2026-03-25")

    with pytest.raises(ValueError, match="Disciplina não pode ser vazia"):
        gerenciador.editar_tarefa(id_tarefa, disciplina="")


def test_editar_tarefa_com_prioridade_invalida_lanca_erro():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Tarefa", "C14", "Desc", "alta", "2026-03-25")

    with pytest.raises(ValueError, match="Prioridade inválida"):
        gerenciador.editar_tarefa(id_tarefa, prioridade="urgente")


def test_remover_tarefa_inexistente_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Tarefa não encontrada"):
        gerenciador.remover_tarefa(999)


def test_concluir_tarefa_inexistente_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Tarefa não encontrada"):
        gerenciador.concluir_tarefa(999)


def test_concluir_tarefa_ja_concluida_lanca_erro():
    gerenciador = GerenciadorTarefas()
    id_tarefa = gerenciador.criar_tarefa("Tarefa", "C14", "Desc", "alta", "2026-03-25")

    gerenciador.concluir_tarefa(id_tarefa)

    with pytest.raises(ValueError, match="Tarefa já está concluída"):
        gerenciador.concluir_tarefa(id_tarefa)


def test_filtrar_por_prioridade_invalida_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Prioridade inválida"):
        gerenciador.filtrar_por_prioridade("urgente")


def test_filtrar_por_status_invalido_lanca_erro():
    gerenciador = GerenciadorTarefas()

    with pytest.raises(ValueError, match="Status inválido"):
        gerenciador.filtrar_por_status("cancelada")
