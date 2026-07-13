#include <stdio.h>
#include <stdlib.h>

// Estrutura do nó da árvore
typedef struct Node {
    int data;
    struct Node* left;
    struct Node* right;
} Node;

// Função para criar um novo nó
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Função para inserir um novo valor na árvore
Node* insert(Node* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    return root;
}

// Função para calcular a soma de todos os elementos da árvore
int somaElementos(Node* root) {
    if (root == NULL) {
        return 0;
    }
    return root->data + somaElementos(root->left) + somaElementos(root->right);
}

// Função para contar a quantidade total de nós na árvore
int contarNos(Node* root) {
    if (root == NULL) {
        return 0;
    }
    return 1 + contarNos(root->left) + contarNos(root->right);
}

// Função para calcular a média dos elementos da árvore
float media(Node* root) {
    int soma = somaElementos(root);
    int quantidade = contarNos(root);
    if (quantidade == 0) {
        return 0;
    }
    return (float)soma / quantidade;
}

// Função principal
int main() {
    Node* root = NULL;
    int value;

    // Leitura dos valores de entrada até -1
    while (1) {
        scanf("%d", &value);
        if (value == -1) {
            break;
        }
        root = insert(root, value);
    }

    // Calcular e imprimir a média
    printf("Media: %.2f\n", media(root));

    return 0;
}
