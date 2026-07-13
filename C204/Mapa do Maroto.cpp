#include <iostream>
#include <vector>

using namespace std;

// Função para adicionar uma aresta ao grafo
void adicionarAresta(vector<vector<int> >& grafo, int origem, int destino) {
    grafo[origem].push_back(destino);
}

// Função para imprimir a lista de adjacências
void imprimirListaAdjacencias(const vector<vector<int> >& grafo) {
    for (int i = 0; i < grafo.size(); ++i) {
        cout << i << " ";
        for (int j = 0; j < grafo[i].size(); ++j) {
            cout << grafo[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    int numVertices, orientado;
    cin >> numVertices >> orientado;

    // Inicialização da lista de adjacências
    vector<vector<int> > grafo(numVertices);

    int origem, destino, peso;
    while (true) {
        cin >> origem >> destino >> peso;
        if (origem == -1 && destino == -1 && peso == -1) {
            break;
        }
        adicionarAresta(grafo, origem, destino);
        // Se o grafo não é orientado, adicionamos também a aresta inversa
        if (orientado == 0) {
            adicionarAresta(grafo, destino, origem);
        }
    }

    // Imprimir a lista de adjacências
    imprimirListaAdjacencias(grafo);

    return 0;
}
