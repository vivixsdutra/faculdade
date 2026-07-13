#include <iostream>
#include <vector>
#include <list>
#include <climits>
#include <algorithm>
using namespace std;

struct Aresta {
    int destino, custo;
};

void dfs(vector<vector<Aresta> >& grafo, int u, vector<bool>& visitado) {
    visitado[u] = true;
    for (vector<Aresta>::iterator it = grafo[u].begin(); it != grafo[u].end(); ++it) {
        Aresta& aresta = *it;
        if (!visitado[aresta.destino]) {
            dfs(grafo, aresta.destino, visitado);
        }
    }
}

int custoMinimo(vector<vector<Aresta> >& grafo) {
    int N = grafo.size();
    vector<bool> visitado(N, false);
    dfs(grafo, 0, visitado);

    for (size_t i = 0; i < visitado.size(); ++i) {
        if (!visitado[i]) {
            return -1; // Se houver vértices não alcançados, significa que o grafo não está conectado
        }
    }

    int custo_total = 0;
    for (size_t u = 0; u < grafo.size(); ++u) {
        for (vector<Aresta>::iterator it = grafo[u].begin(); it != grafo[u].end(); ++it) {
            Aresta& aresta = *it;
            custo_total += aresta.custo;
        }
    }

    // O custo total da árvore geradora mínima é metade do custo total do grafo não direcionado
    return custo_total / 2;
}

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<Aresta> > grafo(N);

    for (int i = 0; i < M; ++i) {
        int u, v, custo;
        cin >> u >> v >> custo;
        Aresta a1 = {v - 1, custo}; // Subtraindo 1 de v para fazer com que os índices comecem de 0
        Aresta a2 = {u - 1, custo}; // Subtraindo 1 de u para fazer com que os índices comecem de 0
        grafo[u - 1].push_back(a1); // Adiciona as arestas ao vetor correspondente
        grafo[v - 1].push_back(a2);
    }

    int custo_total = custoMinimo(grafo);
    if (custo_total == -1) 
        cout << custo_total << endl;
    

    return 0;
}
