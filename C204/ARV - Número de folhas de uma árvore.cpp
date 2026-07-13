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

// Função para contar o número de folhas da árvore
int contaFolhas(Node* root) {
    if (root == NULL) {
        return 0;
    }
    if (root->left == NULL && root->right == NULL) {
        return 1; // O nó é uma folha
    }
    return contaFolhas(root->left) + contaFolhas(root->right);
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

    // Contar o número de folhas da árvore
    printf("%d\n", contaFolhas(root));

    return 0;
}
