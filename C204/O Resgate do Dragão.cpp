#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Função para adicionar uma aresta ao grafo não direcionado
void adicionarAresta(vector<int>* adj, int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);
}

// Função para encontrar o menor caminho entre a sala de entrada e a sala do dragão
int menorCaminho(vector<int>* adj, int N, int entrada, int dragao) {
    vector<bool> visitado(N + 1, false);
    vector<int> distancia(N + 1, 0);

    queue<int> fila;
    fila.push(entrada);
    visitado[entrada] = true;

    while (!fila.empty()) {
        int salaAtual = fila.front();
        fila.pop();

        if (salaAtual == dragao) {
            return distancia[salaAtual] + 1;
        }

        for (int i = 0; i < adj[salaAtual].size(); ++i) {
            int salaAdjacente = adj[salaAtual][i];
            if (!visitado[salaAdjacente]) {
                visitado[salaAdjacente] = true;
                distancia[salaAdjacente] = distancia[salaAtual] + 1;
                fila.push(salaAdjacente);
            }
        }
    }

    return -1; // Não há caminho possível
}

int main() {
    int N, M;
    cin >> N >> M;

    // Inicialização da lista de adjacências
    vector<int>* adj = new vector<int>[N + 1];

    // Leitura das arestas
    int u, v;
    for (int i = 0; i < M; ++i) {
        cin >> u >> v;
        adicionarAresta(adj, u, v);
    }

    // Leitura da sala de entrada e sala do dragão
    int entrada, dragao;
    cin >> entrada >> dragao;

    // Encontrar o menor caminho entre a sala de entrada e a sala do dragão
    int menorDistancia = menorCaminho(adj, N, entrada, dragao);

    // Imprimir resultado
    if (menorDistancia == -1) {
        cout << "IMPOSSIVEL" << endl;
    } else {
        cout << menorDistancia << endl;
    }

    delete[] adj; // Liberar memória alocada para a lista de adjacências

    return 0;
}
