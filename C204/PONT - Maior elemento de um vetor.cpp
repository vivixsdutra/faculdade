#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    // Alocando dinamicamente o vetor de inteiros com tamanho N
    int *vetor = new int[N];

    // Lendo os elementos e inserindo no vetor
    for (int i = 0; i < N; ++i) {
        cin >> vetor[i];
    }

    // Inicializando o maior elemento como o primeiro elemento do vetor
    int maior = vetor[0];

    // Varrendo o vetor usando um ponteiro e encontrando o maior elemento
    for (int i = 1; i < N; ++i) {
        if (vetor[i] > maior) {
            maior = vetor[i];
        }
    }

    // Exibindo o maior elemento encontrado
    cout << maior << endl;

    // Liberando a memória alocada
    delete[] vetor;

    return 0;
}
