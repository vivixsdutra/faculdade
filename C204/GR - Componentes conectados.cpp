#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Estrutura para representar uma aresta
struct Aresta {
    int destino;
};

// Lista de adjacência para representar o grafo
vector<vector<Aresta> > adj_list;

// Função para verificar se o grafo é conexo usando busca em largura
bool bfs(int start) {
    // Vetor para marcar os vértices visitados
    vector<bool> visitado(adj_list.size(), false);

    // Fila para a busca em largura
    queue<int> fila;

    // Inicia a busca a partir do vértice inicial
    fila.push(start);
    visitado[start] = true;

    // Processa todos os vértices alcançáveis a partir do vértice inicial
    while (!fila.empty()) {
        int u = fila.front();
        fila.pop();

        // Percorre todos os vértices adjacentes ao vértice atual
        for (int i = 0; i < adj_list[u].size(); ++i) {
            int v = adj_list[u][i].destino;
            // Se o vértice adjacente ainda não foi visitado, marca como visitado e adiciona à fila
            if (!visitado[v]) {
                visitado[v] = true;
                fila.push(v);
            }
        }
    }

    // Verifica se todos os vértices foram visitados
    for (int i = 0; i < visitado.size(); ++i) {
        if (!visitado[i]) {
            return false; // Se algum vértice não foi visitado, o grafo não é conexo
        }
    }
    return true; // Se todos os vértices foram visitados, o grafo é conexo
}

int main() {
    int num_vertices, start;
    cin >> num_vertices >> start;

    // Inicialização da lista de adjacência
    adj_list.resize(num_vertices);

    // Leitura das arestas do grafo
    int origem, destino;
    while (cin >> origem >> destino) {
        if (origem == -1 && destino == -1) {
            break; // Fim da entrada
        }
        adj_list[origem].push_back({destino});
        adj_list[destino].push_back({origem}); // Grafo não direcionado
    }

    // Verifica se o grafo é conexo a partir do vértice inicial
    if (bfs(start)) {
        cout << "Conexo" << endl;
    } else {
        cout << "Nao conexo" << endl;
    }

    return 0;
}
