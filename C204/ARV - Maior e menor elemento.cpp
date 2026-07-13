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

// Função para encontrar o maior elemento da árvore
int maior(Node* root) {
    if (root == NULL) {
        return -1; // Indica árvore vazia
    }
    Node* current = root;
    while (current->right != NULL) {
        current = current->right;
    }
    return current->data;
}

// Função para encontrar o menor elemento da árvore
int menor(Node* root) {
    if (root == NULL) {
        return -1; // Indica árvore vazia
    }
    Node* current = root;
    while (current->left != NULL) {
        current = current->left;
    }
    return current->data;
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

    // Encontrar o menor e maior elemento
    int menorValor = menor(root);
    int maiorValor = maior(root);

    // Imprimir o menor e maior elemento
    printf("%d e %d\n", menorValor, maiorValor);

    return 0;
}
