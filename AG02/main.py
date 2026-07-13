"""
AG2 - Classificacao de Flores Iris
Instituto Nacional de Telecomunicacoes - Inatel
Engenharia de Software

Este script implementa um classificador de especies de flores Iris utilizando
o algoritmo k-Nearest Neighbors (k-NN) sobre o dataset classico de Ronald Fisher.

Autores: Vitória e José Carlos
Data: Novembro/2025
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings

# Suprimir avisos desnecessarios para uma saida mais limpa
warnings.filterwarnings('ignore')


def print_header(titulo, caractere='=', largura=80):
    """
    Imprime um cabecalho formatado.
    
    Parametros:
        titulo (str): Texto do cabecalho
        caractere (str): Caractere para a linha decorativa
        largura (int): Largura total do cabecalho
    """
    print('\n' + caractere * largura)
    print(titulo.center(largura))
    print(caractere * largura)


def print_section(titulo, largura=80):
    """
    Imprime um titulo de secao formatado.
    
    Parametros:
        titulo (str): Texto da secao
        largura (int): Largura total da linha
    """
    print('\n' + '-' * largura)
    print(titulo)
    print('-' * largura)


def carregar_dados(caminho_arquivo='data.csv'):
    """
    ETAPA 1 e 2: Carrega o dataset Iris a partir de um arquivo CSV.
    
    O dataset Iris contem 150 amostras de flores com 4 atributos numericos
    (comprimento e largura de sepalas e petalas) e a especie como classe.
    
    Parametros:
        caminho_arquivo (str): Caminho para o arquivo CSV com os dados
        
    Retorna:
        DataFrame: Dataset carregado ou None em caso de erro
    """
    print_header('AG2 - CLASSIFICACAO DE ESPECIES DE FLORES IRIS')
    print_section('[ETAPA 1-2] Carregamento do Conjunto de Dados')
    
    try:
        # Leitura do CSV usando Pandas
        df = pd.read_csv(caminho_arquivo)
        
        print('Status: Dados carregados com sucesso')
        print(f'Total de amostras: {len(df)}')
        print(f'Colunas encontradas: {", ".join(df.columns)}')
        print('\nPrevia dos dados (primeiras 5 linhas):')
        print(df.head().to_string(index=False))
        
        return df
        
    except FileNotFoundError:
        print(f'ERRO: Arquivo "{caminho_arquivo}" nao encontrado.')
        print('Certifique-se de que o arquivo CSV esta no mesmo diretorio.')
        return None
        
    except Exception as e:
        print(f'ERRO ao carregar dados: {e}')
        return None


def converter_especies(df):
    """
    ETAPA 3: Converte os nomes das especies (strings) para valores inteiros.
    
    Mapeamento conforme especificado no PDF:
        - 'Iris-setosa'     -> 1
        - 'Iris-versicolor' -> 2
        - 'Iris-virginica'  -> 3
    
    Parametros:
        df (DataFrame): Dataset com a coluna 'species' em formato string
        
    Retorna:
        DataFrame: Dataset com 'species' convertida para inteiros
    """
    print_section('[ETAPA 3] Conversao de Especies para Valores Numericos')
    
    # Mapeamento conforme tabela fornecida
    mapeamento_especies = {
        'Iris-setosa': 1,
        'Iris-versicolor': 2,
        'Iris-virginica': 3
    }
    
    # Aplicar conversao usando replace 
    df['species'] = df['species'].replace(mapeamento_especies)
    
    # Verificacao de sucesso da conversao
    if df['species'].dtype == 'int64':
        print('Status: Conversao realizada com sucesso')
        print('\nDistribuicao das classes no dataset:')
        contagem = df['species'].value_counts().sort_index()
        for codigo, count in contagem.items():
            especie_nome = [k for k, v in mapeamento_especies.items() if v == codigo][0]
            print(f'  Classe {codigo} ({especie_nome:20s}): {count} amostras')
        
        print('\nMapeamento utilizado:')
        for especie, codigo in mapeamento_especies.items():
            print(f'  {especie:20s} -> {codigo}')
    else:
        print('AVISO: Conversao pode ter falhado. Verifique os dados.')
        
    return df


def treinar_modelo(X_train, y_train):
    """
    ETAPA 4: Cria e treina o modelo k-Nearest Neighbors (k-NN).
    
    O k-NN foi escolhido por ser um algoritmo simples, eficaz e interpretavel
    para problemas de classificacao multiclasse como este.
    
    Parametros:
        X_train: Features de treinamento (80% dos dados)
        y_train: Labels de treinamento (80% dos dados)
        
    Retorna:
        modelo treinado
    """
    print_section('[ETAPA 4] Selecao e Configuracao do Modelo')
    
    # Criacao do modelo k-NN com 5 vizinhos (valor padrao comum)
 
    modelo = KNeighborsClassifier(n_neighbors=5)
    
    print('Modelo selecionado: k-Nearest Neighbors (k-NN)')
    print('Parametros:')
    print('  - Numero de vizinhos (k): 5')
    print('  - Metrica de distancia: Euclidiana')
    print('  - Pesos: Uniforme')
    
    print('\nStatus: Iniciando treinamento do modelo...')
    
    # Treinamento do modelo (80% dos dados)
    modelo.fit(X_train, y_train)
    
    print(f'Status: Treinamento concluido com sucesso')
    print(f'Amostras utilizadas no treinamento: {len(X_train)}')
    
    return modelo


def avaliar_modelo(modelo, X_test, y_test):
    """
    ETAPA 5 e 6: Avalia o modelo treinado e exibe metricas detalhadas.
    
    Realiza predicoes nos dados de teste (20%) e calcula metricas como
    acuracia, precisao, recall e F1-score para avaliar o desempenho.
    
    Parametros:
        modelo: Modelo treinado
        X_test: Features de teste (20% dos dados)
        y_test: Labels de teste (20% dos dados)
    """
    print_section('[ETAPA 5-6] Avaliacao do Modelo')
    
    # Realizar predicoes nos dados de teste
    print('Status: Realizando predicoes no conjunto de teste...')
    y_pred = modelo.predict(X_test)
    print(f'Status: Predicoes concluidas para {len(X_test)} amostras\n')
    
    # Calcular acuracia 
    acuracia = accuracy_score(y_test, y_pred)
    
    print('=' * 80)
    print(f'ACURACIA DO MODELO: {acuracia*100:.2f}%'.center(80))
    print('=' * 80)
    
    # Relatorio detalhado de classificacao
    print('\nRELATORIO DETALHADO DE CLASSIFICACAO:')
    print('-' * 80)
    
    nomes_classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    relatorio = classification_report(
        y_test, 
        y_pred,
        target_names=nomes_classes,
        labels=[1, 2, 3],
        zero_division=0
    )
    print(relatorio)
    
    # Matriz de confusao para analise mais profunda
    print('MATRIZ DE CONFUSAO:')
    print('-' * 80)
    matriz_confusao = confusion_matrix(y_test, y_pred, labels=[1, 2, 3])
    
    print('\n                    Predicao')
    print('              Setosa  Versicolor  Virginica')
    print('            ' + '-' * 35)
    labels_reais = ['Setosa    ', 'Versicolor', 'Virginica ']
    for i, linha in enumerate(matriz_confusao):
        print(f'Real {labels_reais[i]} |  {linha[0]:4d}      {linha[1]:4d}        {linha[2]:4d}')
    
    print('\n' + '=' * 80)


def classificar_nova_amostra(modelo):
    """
    ETAPA 7: Permite ao usuario inserir dados arbitrarios para classificacao.
    
    O usuario insere as 4 medidas da flor (comprimento e largura de sepalas
    e petalas) e o modelo prediz a especie baseado no conhecimento adquirido
    durante o treinamento.
    
    Parametros:
        modelo: Modelo treinado pronto para predicoes
    """
    print_header('[ETAPA 7] CLASSIFICADOR INTERATIVO', largura=80)
    print('Este modulo permite classificar novas amostras de flores Iris')
    print('com base nas medidas fornecidas pelo usuario.')
    
    # Mapeamento reverso: codigo -> nome da especie
    mapeamento_reverso = {
        1: "Iris-setosa",
        2: "Iris-versicolor",
        3: "Iris-virginica"
    }
    
    while True:
        print('\n' + '=' * 80)
        print('Insira as medidas da flor (em centimetros):')
        print('-' * 80)
        
        try:
            # Coletar as 4 features do usuario
            sepal_length = float(input('Comprimento da Sepala (cm): '))
            sepal_width = float(input('Largura da Sepala (cm): '))
            petal_length = float(input('Comprimento da Petala (cm): '))
            petal_width = float(input('Largura da Petala (cm): '))
            
            # Validacao basica dos valores
            if any(v <= 0 for v in [sepal_length, sepal_width, petal_length, petal_width]):
                print('\nERRO: Todas as medidas devem ser valores positivos.')
                print('Por favor, tente novamente.')
                continue
            
            # Preparar dados para predicao (formato 2D necessario)
            nova_amostra = [[sepal_length, sepal_width, petal_length, petal_width]]
            
            # Realizar predicao usando o modelo treinado
            predicao_codigo = modelo.predict(nova_amostra)[0]
            
            # Obter nome da especie
            especie_predita = mapeamento_reverso.get(predicao_codigo, "Desconhecida")
            
            # Exibir resultado
            print('\n' + '=' * 80)
            print('RESULTADO DA CLASSIFICACAO'.center(80))
            print('=' * 80)
            print(f'\nEspecie predita: {especie_predita}')
            print(f'Codigo numerico: {predicao_codigo}')
            
            # Probabilidades 
            if hasattr(modelo, 'predict_proba'):
                probabilidades = modelo.predict_proba(nova_amostra)[0]
                print('\nDistribuicao de probabilidades:')
                print('-' * 80)
                for idx, (especie, prob) in enumerate(zip(mapeamento_reverso.values(), probabilidades), 1):
                    barra = '#' * int(prob * 50)
                    print(f'  {especie:20s} [{prob*100:5.2f}%] {barra}')
            
            print('=' * 80)
            
        except ValueError:
            print('\nERRO: Por favor, insira apenas valores numericos validos.')
            print('Exemplo: 5.1, 3.5, 1.4, 0.2')
            continue
            
        except Exception as e:
            print(f'\nERRO inesperado: {e}')
            continue
        
        # Perguntar se deseja classificar outra amostra
        print('\n' + '-' * 80)
        continuar = input('Deseja classificar outra flor? (s/n): ').lower().strip()
        
        if continuar not in ['s', 'sim', 'y', 'yes']:
            print('\nEncerrando o classificador.')
            break


def main():
    """
    Funcao principal que orquestra todas as etapas do projeto AG2.
    
    Fluxo completo:
        1. Carregar dados do CSV
        2. Converter especies para valores numericos
        3. Escolher e configurar o modelo
        4. Separar dados em treino (80%) e teste (20%)
        5. Treinar o modelo
        6. Avaliar e exibir metricas
        7. Permitir classificacao de dados arbitrarios
    """
    
    # ETAPA 1-2: Carregar dados
    df = carregar_dados('data.csv')
    if df is None:
        return
    
    # ETAPA 3: Converter especies para inteiros
    df = converter_especies(df)
    
    # Separar features (X) e target (y)
    # Features: 4 medidas numericas da flor
    X = df.drop('species', axis=1)
    # Target: especie (1, 2 ou 3)
    y = df['species']
    
    # ETAPA 5: Separar em conjuntos de treino e teste
    # 80% para treinamento, 20% para teste
    # shuffle=True garante o embaralhamento 
    # random_state=42 garante reprodutibilidade dos resultados
    print_section('[ETAPA 5] Separacao dos Dados em Treino e Teste')
    
    print('Configuracao da separacao:')
    print('  - Proporcao treino/teste: 80% / 20%')
    print('  - Embaralhamento: Ativado (shuffle=True)')
    print('  - Semente aleatoria: 42 (para reprodutibilidade)')
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,      # 20% para teste
        shuffle=True,       # Embaralhar 
        random_state=42     # Reprodutibilidade
    )
    
    print(f'\nResultado da separacao:')
    print(f'  - Conjunto de treino: {len(X_train)} amostras ({len(X_train)/len(df)*100:.1f}%)')
    print(f'  - Conjunto de teste:  {len(X_test)} amostras ({len(X_test)/len(df)*100:.1f}%)')
    
    # ETAPA 4-5: Treinar modelo
    modelo = treinar_modelo(X_train, y_train)
    
    # ETAPA 5-6: Avaliar modelo
    avaliar_modelo(modelo, X_test, y_test)
    
    # ETAPA 7: Classificacao interativa
    classificar_nova_amostra(modelo)
    

# Ponto de entrada do programa
if __name__ == "__main__":
    main()