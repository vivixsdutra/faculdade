# Teste de API com Postman (S206 - Qualidade de Software)

Este repositório contém o projeto da prova da disciplina **S206 - Qualidade de Software**, orientada pelo Prof. Christopher Lima. A proposta consiste em realizar **testes de API utilizando o Postman** e gerar um relatório em HTML com o **Newman**.

## 📌 Descrição da Prova

A tarefa consiste em desenvolver **três cenários de teste diferentes** utilizando uma API pública (neste caso, **The Cat API**). Os testes devem seguir os seguintes critérios:

- ✅ Utilizar a ferramenta **Postman**
- ✅ Desenvolver **no mínimo 3 cenários de teste**
- ✅ Pelo menos **1 cenário negativo** (erro proposital)
- ✅ Pelo menos **1 requisição que **não seja do tipo GET**
- ✅ Não usar environment (variáveis globais)
- ✅ Utilizar uma API diferente das já usadas em exercícios anteriores
- ✅ Entregar um **relatório em HTML** utilizando o **Newman**
- ✅ Entregar o projeto via **GitHub**, com este README explicativo

---

## 🧪 API Utilizada

- Nome: **The Cat API**
- Site: [https://thecatapi.com](https://thecatapi.com)
- Documentação: [https://docs.thecatapi.com](https://docs.thecatapi.com)

---

## ✅ Casos de Teste Criados

| Nome do Teste         | Método | Descrição                                                                 |
|------------------------|--------|---------------------------------------------------------------------------|
| `GET_Breeds`           | GET    | Lista todas as raças de gatos disponíveis na API                         |
| `POST_VotoValido`      | POST   | Envia um voto positivo para uma imagem de gato (requisição válida)       |
| `POST_VotoInvalido`    | POST   | Envia um voto sem `image_id`, gerando erro (teste negativo proposital)   |

Todos os testes foram escritos na aba `Tests` do Postman para validar automaticamente o status da resposta e os campos retornados.

---

## 🗂️ Estrutura do Projeto

```
📁 Prova_S206_CatAPI/
├── Prova_S206_CatAPI.postman_collection.json
├── newman/
│   └── newman-run-report.html
└── README.md
```

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/Prova_S206_CatAPI.git
cd Prova_S206_CatAPI
```

### 2. Instalar o Newman

Se ainda não tiver o [Node.js](https://nodejs.org) instalado, instale primeiro. Depois, instale o Newman com:

```bash
npm install -g newman
```

### 3. Executar os Testes e Gerar o Relatório

```bash
newman run Prova_S206_CatAPI.postman_collection.json -r html --reporter-html-export newman/newman-run-report.html
```

Isso gerará um relatório HTML na pasta `newman/`, com os resultados dos testes automatizados.

---

## 📄 Observações Finais

- **Não foi utilizado environment**, conforme exigido
- Todos os testes são executáveis diretamente com a API Key colada manualmente nos headers
- A coleção foi exportada no formato **Postman Collection v2.1**
- O relatório HTML está pronto para ser entregue ou revisado

---

## ✍️ Autor

- **Vitória Dutra**
- Engenharia de Software - S206
- Professor: Christopher Lima
