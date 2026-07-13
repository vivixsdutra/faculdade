#include <iostream>
using namespace std;

// Definição da estrutura para representar um nó da árvore
struct No {
    int valor;
    No* esquerda;
    No* direita;

    No(int val) : valor(val), esquerda(NULL), direita(NULL) {}
};

// Função para inserir um número na árvore
No* inserir(No* raiz, int valor) {
    if (raiz == NULL) {
        return new No(valor);
    }
    if (valor < raiz->valor) {
        raiz->esquerda = inserir(raiz->esquerda, valor);
    } else if (valor > raiz->valor) {
        raiz->direita = inserir(raiz->direita, valor);
    }
    return raiz;
}

// Função para buscar um número na árvore
bool buscar(No* raiz, int valor) {
    if (raiz == NULL) {
        return false;
    }
    if (raiz->valor == valor) {
        return true;
    } else if (valor < raiz->valor) {
        return buscar(raiz->esquerda, valor);
    } else {
        return buscar(raiz->direita, valor);
    }
}

int main() {
    int N, X;
    cin >> N;
    No* raiz = NULL;

    // Inserindo os N números na árvore
    for (int i = 0; i < N; ++i) {
        int num;
        cin >> num;
        raiz = inserir(raiz, num);
    }

    // Lendo o número X a ser procurado
    cin >> X;

    // Verificando se X está na árvore
    if (buscar(raiz, X)) {
        cout << "Encontrado" << endl;
    } else {
        cout << "Nao encontrado" << endl;
    }

    return 0;
}
