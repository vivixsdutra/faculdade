#include <iostream>
#include <list>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

struct no {
    int destino;
};

void dfs_visit(list<no> adj[], int u, bool visitado[], stack<int>& pilha) {
    visitado[u] = true;
    for (list<no>::iterator it = adj[u].begin(); it != adj[u].end(); ++it) {
        if (!visitado[it->destino]) {
            dfs_visit(adj, it->destino, visitado, pilha);
        }
    }
    pilha.push(u);
}

void dfs(list<no> adj[], int nVertices, stack<int>& pilha) {
    bool* visitado = new bool[nVertices];
    for (int i = 0; i < nVertices; ++i) {
        visitado[i] = false;
    }

    for (int i = 0; i < nVertices; ++i) {
        if (!visitado[i]) {
            dfs_visit(adj, i, visitado, pilha);
        }
    }

    delete[] visitado;
}

void ordenacao_topologica(list<no> adj[], int nVertices) {
    stack<int> pilha;
    dfs(adj, nVertices, pilha);

    cout << "";
    while (!pilha.empty()) {
        cout << " " << pilha.top();
        pilha.pop();
    }
    cout << endl;
}

int main() {
    int nVertices, orientado;
    cin >> nVertices >> orientado;

    list<no> adj[nVertices];
    int origem, destino;
    while (cin >> origem >> destino && origem != -1 && destino != -1) {
        no novoNo;
        novoNo.destino = destino;
        adj[origem].push_back(novoNo);
    }

    ordenacao_topologica(adj, nVertices);

    return 0;
}
