#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

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

// Função para encontrar o nó mínimo na árvore
Node* findMin(Node* root) {
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

// Função para remover um valor da árvore
Node* removeNode(Node* root, int data) {
    if (root == NULL) {
        return NULL;
    }
    if (data < root->data) {
        root->left = removeNode(root->left, data);
    } else if (data > root->data) {
        root->right = removeNode(root->right, data);
    } else {
        // Nó com apenas um filho ou nenhum
        if (root->left == NULL) {
            Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            Node* temp = root->left;
            free(root);
            return temp;
        }

        // Nó com dois filhos
        Node* temp = findMin(root->right);
        root->data = temp->data;
        root->right = removeNode(root->right, temp->data);
    }
    return root;
}

// Função para buscar um valor na árvore
bool search(Node* root, int data) {
    if (root == NULL) {
        return false;
    }
    if (root->data == data) {
        return true;
    } else if (data < root->data) {
        return search(root->left, data);
    } else {
        return search(root->right, data);
    }
}

// Função principal
int main() {
    int N;
    scanf("%d", &N);
    
    Node* root = NULL;
    
    for (int i = 0; i < N; i++) {
        char operation;
        int x;
        scanf(" %c %d", &operation, &x);
        
        if (operation == 'i') {
            root = insert(root, x);
        } else if (operation == 'r') {
            root = removeNode(root, x);
        } else if (operation == 'b') {
            if (search(root, x)) {
                printf("Sim\n");
            } else {
                printf("Não\n");
            }
        }
    }
    
    return 0;
}
