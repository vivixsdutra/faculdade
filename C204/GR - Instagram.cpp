#include <iostream>
#include <list>

using namespace std;

// Função para imprimir os seguidores de um usuário
void imprimirSeguidores(string nomes[], const list<int> grafo[], int usuario, int N) {
    // Verifica se o usuário existe
    if (usuario >= N) {
        cout << "Usuário não encontrado" << endl;
        return;
    }

    // Imprime os nomes dos seguidores do usuário
    cout << "Seguidores de " << nomes[usuario] << ":" << endl;
    for (list<int>::const_iterator it = grafo[usuario].begin(); it != grafo[usuario].end(); ++it) {
        cout << nomes[*it] << endl;
    }
}

int main() {
    int N;
    cin >> N;

    // Vetor para armazenar os nomes dos usuários
    string nomes[N];
    for (int i = 0; i < N; ++i) {
        cin.ignore(); // Limpa o buffer de entrada
        getline(cin, nomes[i]);
    }

    // Vetor de listas para representar o grafo
    list<int> grafo[N];

    // Leitura dos seguidores de cada usuário
    int seguidor;
    for (int i = 0; i < N; ++i) {
        while (true) {
            cin >> seguidor;
            if (seguidor == -1) {
                break;
            }
            grafo[seguidor].push_back(i); // i segue seguidor
        }
    }

    // Usuário para verificar os seguidores
    int usuario_desejado;
    cin >> usuario_desejado;

    // Imprime os seguidores do usuário desejado
    imprimirSeguidores(nomes, grafo, usuario_desejado, N);

    return 0;
}
