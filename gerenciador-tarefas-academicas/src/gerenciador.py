class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = {}
        self.proximo_id = 1

    def criar_tarefa(self, titulo, disciplina, descricao, prioridade, prazo):
        if not titulo or titulo.strip() == "":
            raise ValueError("Título não pode ser vazio")

        if not disciplina or disciplina.strip() == "":
            raise ValueError("Disciplina não pode ser vazia")

        prioridades_validas = ["baixa", "media", "alta"]
        if prioridade not in prioridades_validas:
            raise ValueError("Prioridade inválida")

        tarefa = {
            "titulo": titulo,
            "disciplina": disciplina,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": "pendente",
            "prazo": prazo
        }

        id_tarefa = self.proximo_id
        self.tarefas[id_tarefa] = tarefa
        self.proximo_id += 1

        return id_tarefa

    def buscar_tarefa(self, id_tarefa):
        if id_tarefa not in self.tarefas:
            raise ValueError("Tarefa não encontrada")

        return self.tarefas[id_tarefa]

    def listar_tarefas(self):
        return self.tarefas

    def editar_tarefa(self, id_tarefa, titulo=None, disciplina=None, descricao=None, prioridade=None, prazo=None):
        if id_tarefa not in self.tarefas:
            raise ValueError("Tarefa não encontrada")

        tarefa = self.tarefas[id_tarefa]

        if titulo is not None:
            if titulo.strip() == "":
                raise ValueError("Título não pode ser vazio")
            tarefa["titulo"] = titulo

        if disciplina is not None:
            if disciplina.strip() == "":
                raise ValueError("Disciplina não pode ser vazia")
            tarefa["disciplina"] = disciplina

        if descricao is not None:
            tarefa["descricao"] = descricao

        if prioridade is not None:
            prioridades_validas = ["baixa", "media", "alta"]
            if prioridade not in prioridades_validas:
                raise ValueError("Prioridade inválida")
            tarefa["prioridade"] = prioridade

        if prazo is not None:
            tarefa["prazo"] = prazo

    def remover_tarefa(self, id_tarefa):
        if id_tarefa not in self.tarefas:
            raise ValueError("Tarefa não encontrada")

        del self.tarefas[id_tarefa]

    def concluir_tarefa(self, id_tarefa):
        if id_tarefa not in self.tarefas:
            raise ValueError("Tarefa não encontrada")

        if self.tarefas[id_tarefa]["status"] == "concluida":
            raise ValueError("Tarefa já está concluída")

        self.tarefas[id_tarefa]["status"] = "concluida"

    def filtrar_por_disciplina(self, disciplina):
        return {
            id_tarefa: tarefa
            for id_tarefa, tarefa in self.tarefas.items()
            if tarefa["disciplina"].lower() == disciplina.lower()
        }

    def filtrar_por_prioridade(self, prioridade):
        prioridades_validas = ["baixa", "media", "alta"]
        if prioridade not in prioridades_validas:
            raise ValueError("Prioridade inválida")

        return {
            id_tarefa: tarefa
            for id_tarefa, tarefa in self.tarefas.items()
            if tarefa["prioridade"] == prioridade
        }

    def filtrar_por_status(self, status):
        status_validos = ["pendente", "em andamento", "concluida"]
        if status not in status_validos:
            raise ValueError("Status inválido")

        return {
            id_tarefa: tarefa
            for id_tarefa, tarefa in self.tarefas.items()
            if tarefa["status"] == status
        }