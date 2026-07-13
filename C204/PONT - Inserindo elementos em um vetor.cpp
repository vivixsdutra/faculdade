#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    // Alocando dinamicamente o vetor de inteiros com tamanho N
    int *vetor = new int[N];

    // Ponteiro para percorrer o vetor
    int *p = vetor;

    // Lendo os elementos e inserindo no vetor usando o ponteiro
    for (int i = 0; i < N; ++i) {
        cin >> *p;
        p++; // Avança o ponteiro para a próxima posição do vetor
    }

    // Reinicializa o ponteiro para o início do vetor
    p = vetor;

    // Varrendo o vetor usando o ponteiro e exibindo os elementos
    for (int i = 0; i < N; ++i) {
        cout << *p << " ";
        p++; // Avança o ponteiro para a próxima posição do vetor
    }

    // Liberando a memória alocada
    delete[] vetor;

    return 0;
}
