#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Função para criar a matriz de adjacência
vector<vector<int> > criarMatrizAdjacencia(int N, const vector<pair<int, int> >& caminhos) {
    vector<vector<int> > matrizAdjacencia(N, vector<int>(N, 0)); // Inicializa a matriz com 0s
    for (int i = 0; i < caminhos.size(); ++i) {
        int A = caminhos[i].first;
        int B = caminhos[i].second;
        matrizAdjacencia[A - 1][B - 1] = 1; // Marca o caminho entre A e B como 1
        matrizAdjacencia[B - 1][A - 1] = 1; // Considerando os caminhos como bidirecionais
    }
    return matrizAdjacencia;
}

// Função para encontrar cidades inacessíveis a partir de uma determinada cidade X
vector<int> cidadesInacessiveis(int X, int Y, int N, const vector<vector<int> >& matrizAdjacencia) {
    vector<bool> visitado(N, false);
    vector<int> inacessiveis;
    queue<int> fila;
    
    // Marca a cidade X como visitada, exceto se for a cidade Y
    if (X != Y) {
        visitado[X - 1] = true;
        fila.push(X - 1);
    }

    // Percorre as cidades alcançáveis a partir de X
    while (!fila.empty()) {
        int atual = fila.front();
        fila.pop();
        for (int i = 0; i < N; ++i) {
            if (matrizAdjacencia[atual][i] && !visitado[i]) {
                visitado[i] = true;
                fila.push(i);
            }
        }
    }

    // Todas as cidades não visitadas são inacessíveis a partir de X, exceto Y
    for (int i = 0; i < N; ++i) {
        if (!visitado[i] && i != X - 1 && i != Y - 1) {
            inacessiveis.push_back(i + 1);
        }
    }

    return inacessiveis;
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<pair<int, int> > caminhos(M);
    for (int i = 0; i < M; ++i) {
        cin >> caminhos[i].first >> caminhos[i].second;
    }

    // Criar matriz de adjacência
    vector<vector<int> > matrizAdjacencia = criarMatrizAdjacencia(N, caminhos);

    int X, Y;
    cin >> X >> Y;

    // Encontrar cidades inacessíveis a partir de X
    vector<int> inacessiveis = cidadesInacessiveis(X, Y, N, matrizAdjacencia);

    // Imprimir cidades inacessíveis
    for (size_t i = 0; i < inacessiveis.size(); ++i) {
        cout << inacessiveis[i] << " ";
    }
    cout << endl;

    return 0;
}
