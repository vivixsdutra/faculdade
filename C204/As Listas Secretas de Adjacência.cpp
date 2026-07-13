#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Função para criar a lista de adjacência
vector<vector<int> > criarListaAdjacencia(int N, const vector<pair<int, int> >& caminhos) {
    vector<vector<int> > listaAdjacencia(N + 1); // +1 para compensar o índice base 1
    for (int i = 0; i < caminhos.size(); ++i) {
        int A = caminhos[i].first;
        int B = caminhos[i].second;
        listaAdjacencia[A].push_back(B);
        listaAdjacencia[B].push_back(A); // Considerando os caminhos como bidirecionais
    }
    return listaAdjacencia;
}

// Função para imprimir as cidades conectadas
void imprimirCidadesConectadas(const vector<vector<int> >& listaAdjacencia) {
    for (size_t i = 1; i < listaAdjacencia.size(); ++i) {
        vector<int> vizinhos = listaAdjacencia[i];
        sort(vizinhos.begin(), vizinhos.end()); // Ordena os vizinhos em ordem crescente
        cout << vizinhos.size() << " ";
        for (size_t j = 0; j < vizinhos.size(); ++j) {
            cout << vizinhos[j];
            if (j < vizinhos.size() - 1) {
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

    // Criar lista de adjacência
    vector<vector<int> > listaAdjacencia = criarListaAdjacencia(N, caminhos);

    // Imprimir cidades conectadas
    imprimirCidadesConectadas(listaAdjacencia);

    return 0;
}
