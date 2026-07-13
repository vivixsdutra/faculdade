# AG2 - Classificação de Espécies de Flores Iris

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Sobre o Projeto

Trabalho prático da disciplina AG2 (Engenharias de Computação e Software) do Instituto Nacional de Telecomunicações (Inatel), que implementa um sistema completo de classificação de espécies de flores Iris utilizando técnicas de Machine Learning.

O projeto utiliza o famoso dataset Iris, coletado por Ronald Fisher em 1936, para treinar um modelo capaz de classificar flores em três espécies distintas: **Iris Setosa**, **Iris Versicolor** e **Iris Virginica**.

## 🎯 Objetivos

- Implementar um pipeline completo de Machine Learning
- Aplicar técnicas de pré-processamento de dados
- Treinar e avaliar modelos de classificação
- Criar uma interface interativa para classificação em tempo real
- Documentar código seguindo boas práticas de desenvolvimento

## 🚀 Funcionalidades

- ✅ Carregamento e análise exploratória do dataset
- ✅ Conversão de dados categóricos para numéricos
- ✅ Separação de dados em treino (80%) e teste (20%)
- ✅ Treinamento com algoritmo k-Nearest Neighbors (k-NN)
- ✅ Avaliação detalhada com múltiplas métricas
- ✅ Matriz de confusão para análise de erros
- ✅ Classificador interativo para dados arbitrários
- ✅ Exibição de probabilidades por classe

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **Scikit-learn**: Biblioteca de Machine Learning
- **NumPy**: Computação numérica (dependência indireta)

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/AG02
cd AG02
```

2. **Crie um ambiente virtual** (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install pandas scikit-learn
```

4. **Prepare o dataset**

O arquivo `data.csv` já está incluído no repositório. Caso necessário, você pode baixá-lo do [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris).

## 💻 Como Usar

### Execução Básica

```bash
python main.py
```

## 🤖 Algoritmo Utilizado

### k-Nearest Neighbors (k-NN)

O k-NN é um algoritmo de aprendizado supervisionado que classifica novos dados baseando-se na "proximidade" com dados conhecidos.

**Características:**
- Algoritmo não-paramétrico
- Simples e interpretável
- Eficaz para problemas multiclasse
- Não requer treinamento complexo

**Parâmetros:**
- `n_neighbors=5`: Considera os 5 vizinhos mais próximos
- `metric='euclidean'`: Distância euclidiana (padrão)

**Por que k-NN?**
- Excelente desempenho no dataset Iris
- Fácil compreensão e explicação
- Adequado para dataset pequeno e balanceado

## 👥 Autores

Vitória de Moraes Dutra e José Carlos Rebouças Neto 

**Instituição**: Instituto Nacional de Telecomunicações (Inatel)  
**Curso**: Engenharia de Software  
**Disciplina**: AG2  
**Professores**: Prof. Me. Marcelo Vinícius Cysneiros Aragão e Prof. Me. Renzo Mesquita Paranaíba

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🔗 Links Úteis

- [Dataset Original - UCI Repository](https://archive.ics.uci.edu/dataset/53/iris)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Documentação Scikit-learn](https://scikit-learn.org/stable/)
- [Artigo Original - Fisher (1936)](https://doi.org/10.1111/j.1469-1809.1936.tb02137.x)
- [k-NN Wikipedia](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)


**Desenvolvido para AG2 - Inatel 2025**
