#include <iostream>
#include <list>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

// Estrutura para representar uma aresta
struct Aresta {
    int destino;
    int peso;
};

// Função para adicionar uma aresta ao grafo direcionado
void adicionarAresta(list<Aresta>* adj, int origem, int destino, int peso) {
    Aresta a;
    a.destino = destino;
    a.peso = peso;
    adj[origem].push_back(a);
}

// Função para implementar o algoritmo de Dijkstra
void dijkstra(list<Aresta>* adj, int nVertices, int start, int end) {
    vector<bool> intree(nVertices, false);
    vector<int> distance(nVertices, INT_MAX);
    vector<int> parent(nVertices, -1);

    distance[start] = 0;
    int v = start;

    while (!intree[v]) {
        intree[v] = true;
        for (int i = 0; i < nVertices; ++i) {
            for (list<Aresta>::iterator it = adj[v].begin(); it != adj[v].end(); ++it) {
                int destino = it->destino;
                int peso = it->peso;
                if (distance[destino] > distance[v] + peso) {
                    distance[destino] = distance[v] + peso;
                    parent[destino] = v;
                }
            }
        }
        v = 0;
        int dist = INT_MAX;
        for (int u = 0; u < nVertices; ++u) {
            if (!intree[u] && dist > distance[u]) {
                dist = distance[u];
                v = u;
            }
        }
    }

    // Reconstruir o caminho mais curto
    vector<int> caminho;
    for (int v = end; v != -1; v = parent[v]) {
        caminho.push_back(v);
    }
    reverse(caminho.begin(), caminho.end());

    // Imprimir o caminho mais curto e seu custo
    cout << "Menor caminho:";
    for (int i = 0; i < caminho.size(); ++i) {
        cout << " " << caminho[i];
    }
    cout << endl;
    cout << "Custo: " << distance[end] << endl;
}

int main() {
    int numVertices, orientado, start, end;
    cin >> numVertices >> orientado >> start >> end;

    // Inicialização da lista de adjacências
    list<Aresta>* adj = new list<Aresta>[numVertices];

    int origem, destino, peso;
    while (true) {
        cin >> origem >> destino >> peso;
        if (origem == -1 && destino == -1 && peso == -1) {
            break;
        }
        adicionarAresta(adj, origem, destino, peso);
    }

    // Encontrar o caminho mais curto usando o algoritmo de Dijkstra
    dijkstra(adj, numVertices, start, end);

    delete[] adj; // Liberar memória alocada para a lista de adjacências

    return 0;
}
