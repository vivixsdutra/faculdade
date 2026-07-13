#include <iostream>
#include <vector>

using namespace std;

// Função recursiva para busca binária
int buscaBinaria(const vector<int> &vetor, int inicio, int fim, int alvo) {
    if (fim >= inicio) {
        int meio = inicio + (fim - inicio) / 2;

        // Se o elemento está presente no meio
        if (vetor[meio] == alvo)
            return meio;

        // Se o elemento está antes do meio
        if (vetor[meio] > alvo)
            return buscaBinaria(vetor, inicio, meio - 1, alvo);

        // Se o elemento está depois do meio
        return buscaBinaria(vetor, meio + 1, fim, alvo);
    }

    // Elemento não encontrado
    return -1;
}

// Função principal para realizar a busca binária em um vetor ordenado
int buscaBinariaVetor(const vector<int> &vetor, int tamanho, int alvo) {
    return buscaBinaria(vetor, 0, tamanho - 1, alvo);
}

int main() 
{
	setlocale(LC_ALL, "Portuguese");
    int N;
    cin >> N;

    vector<int> vetor(N);

    // Entrada dos elementos do vetor
    for (int i = 0; i < N; ++i) {
        cin >> vetor[i];
    }

    int alvo;
    cin >> alvo;

    // Realiza a busca binária no vetor
    int indice = buscaBinariaVetor(vetor, N, alvo);

    // Exibe o resultado da busca
    if (indice != -1)
        cout << indice << endl;
    else
        cout << "-1" << endl;

    return 0;
}
