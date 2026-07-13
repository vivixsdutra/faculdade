#include <iostream>
#include <list>
#include <queue>

using namespace std;

// Estrutura para representar um nó do grafo
struct no {
    int v; // vértice adjacente
    int peso; // peso da aresta (opcional)
};

// Função para realizar o percurso em largura (BFS)
void bfs(list<no> adj[], int nVertices, int s) {
    char state[nVertices]; // estado de cada vértice: 'u' (não descoberto), 'd' (descoberto), 'p' (processado)
    int pai[nVertices]; // pai de cada vértice no percurso

    // Inicializa os estados e os pais de todos os vértices
    for (int u = 0; u < nVertices; ++u) {
        if (u != s) {
            state[u] = 'u'; // undiscovered
            pai[u] = -1; // sem pai
        }
    }

    state[s] = 'd'; // descobre o vértice inicial
    pai[s] = -1;

    // Fila para armazenar os vértices a serem processados
    queue<int> Q;
    Q.push(s);

    // Realiza o percurso em largura
    while (!Q.empty()) {
        int u = Q.front();
        Q.pop();

        cout << u << endl; // Imprime o vértice atual

        // Processa todos os vértices adjacentes a u
        for (list<no>::iterator p = adj[u].begin(); p != adj[u].end(); ++p) {
            int v = p->v; // Vértice adjacente

            // Se o vértice adjacente ainda não foi descoberto, o descobre e o adiciona à fila
            if (state[v] == 'u') {
                state[v] = 'd';
                pai[v] = u;
                Q.push(v);
                cout << u << " " << v << endl; // Imprime a aresta (u, v)
            }
        }

        state[u] = 'p'; // Marca o vértice como processado
    }
}

int main() {
    int nVertices, verticeInicial;
    cin >> nVertices >> verticeInicial;

    // Lista de adjacências para representar o grafo
    list<no> adj[nVertices];

    // Leitura das arestas do grafo
    int origem, destino, peso;
    while (true) {
        cin >> origem >> destino >> peso;
        if (origem == -1 && destino == -1 && peso == -1) {
            break; // Condição de saída
        }
        // Adiciona a aresta (origem, destino) ao grafo
        no novaAresta;
        novaAresta.v = destino;
        novaAresta.peso = peso;
        adj[origem].push_back(novaAresta);
        novaAresta.v = origem;
        adj[destino].push_back(novaAresta); // Se o grafo é não direcionado, adiciona a aresta no sentido oposto também
    }

    // Realiza o percurso em largura a partir do vértice inicial
    bfs(adj, nVertices, verticeInicial);

    return 0;
}
