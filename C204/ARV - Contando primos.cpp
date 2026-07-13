#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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

// Função para verificar se um número é primo
int isPrime(int n) {
    if (n <= 1) {
        return 0;
    }
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

// Função para contar números primos na árvore
int contaPrimos(Node* root) {
    if (root == NULL) {
        return 0;
    }
    int count = isPrime(root->data);
    count += contaPrimos(root->left);
    count += contaPrimos(root->right);
    return count;
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

    // Contagem de números primos na árvore
    printf("%d numeros primos\n", contaPrimos(root));

    return 0;
}
