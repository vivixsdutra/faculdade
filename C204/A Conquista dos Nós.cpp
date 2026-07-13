#include <iostream>
#include <vector>

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

// Função para imprimir a matriz de adjacência
void imprimirMatrizAdjacencia(const vector<vector<int> >& matrizAdjacencia) {
    for (int i = 0; i < matrizAdjacencia.size(); ++i) {
        for (int j = 0; j < matrizAdjacencia[i].size(); ++j) {
            cout << matrizAdjacencia[i][j];
            if (j < matrizAdjacencia[i].size() - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }
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

    // Imprimir matriz de adjacência
    imprimirMatrizAdjacencia(matrizAdjacencia);

    return 0;
}
