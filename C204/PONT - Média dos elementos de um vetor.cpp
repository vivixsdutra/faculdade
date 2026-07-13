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

    // Calculando a soma dos elementos
    int soma = 0;
    for (int i = 0; i < N; ++i) {
        soma += vetor[i];
    }

    // Calculando a média
    double media = static_cast<double>(soma) / N;

    // Exibindo a média com 2 casas decimais
    cout << fixed;
    cout.precision(2);
    cout << media << endl;

    // Liberando a memória alocada
    delete[] vetor;

    return 0;
}
