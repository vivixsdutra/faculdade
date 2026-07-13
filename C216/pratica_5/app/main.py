from fastapi import FastAPI, HTTPException
from app.schemas import AlunoCreate, AlunoUpdate
from app.database import alunos, contadores_matricula

app = FastAPI(title="Gerenciador de Alunos - C216")

CURSOS_VALIDOS = ["GES", "GEC"]


@app.post("/api/v1/alunos/")
def cadastrar_aluno(aluno: AlunoCreate):
    curso = aluno.curso.upper()

    if curso not in CURSOS_VALIDOS:
        raise HTTPException(status_code=400, detail="Curso inválido. Use GES ou GEC.")

    contadores_matricula[curso] += 1
    matricula = contadores_matricula[curso]
    aluno_id = f"{curso}{matricula}"

    novo_aluno = {
        "id": aluno_id,
        "nome": aluno.nome,
        "email": aluno.email,
        "curso": curso,
        "matricula": matricula
    }

    alunos[aluno_id] = novo_aluno

    return novo_aluno


@app.get("/api/v1/alunos/")
def listar_alunos():
    return list(alunos.values())


@app.get("/api/v1/alunos/{aluno_id}")
def buscar_aluno(aluno_id: str):
    aluno_id = aluno_id.upper()

    if aluno_id not in alunos:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    return alunos[aluno_id]


@app.patch("/api/v1/alunos/{aluno_id}")
def atualizar_aluno(aluno_id: str, dados: AlunoUpdate):
    aluno_id = aluno_id.upper()

    if aluno_id not in alunos:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    aluno_atual = alunos[aluno_id]

    if dados.nome is not None:
        aluno_atual["nome"] = dados.nome

    if dados.email is not None:
        aluno_atual["email"] = dados.email

    if dados.curso is not None:
        novo_curso = dados.curso.upper()

        if novo_curso not in CURSOS_VALIDOS:
            raise HTTPException(status_code=400, detail="Curso inválido. Use GES ou GEC.")

        aluno_atual["curso"] = novo_curso

    return aluno_atual


@app.delete("/api/v1/alunos/{aluno_id}")
def remover_aluno(aluno_id: str):
    aluno_id = aluno_id.upper()

    if aluno_id not in alunos:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")

    aluno_removido = alunos.pop(aluno_id)

    return {
        "mensagem": "Aluno removido com sucesso.",
        "aluno": aluno_removido
    }


@app.delete("/api/v1/alunos/")
def resetar_alunos():
    alunos.clear()

    return {
        "mensagem": "Lista de alunos resetada com sucesso."
    }