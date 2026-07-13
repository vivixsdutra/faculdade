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

// Função para percorrer a árvore em ordem inversa (ordem decrescente) e imprimir os elementos
void inorderReverse(Node* root) {
    if (root != NULL) {
        inorderReverse(root->right);
        printf("%d ", root->data);
        inorderReverse(root->left);
    }
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

    // Percorrer a árvore em ordem inversa (ordem decrescente) e imprimir os elementos
    inorderReverse(root);
    printf("\n");

    return 0;
}
