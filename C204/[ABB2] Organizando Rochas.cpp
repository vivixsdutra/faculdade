#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

// Estrutura para armazenar informações da rocha
typedef struct Rocha {
    char nome[100];
    char tipo[50];
} Rocha;

// Estrutura do nó da árvore
typedef struct Node {
    Rocha rocha;
    struct Node* left;
    struct Node* right;
} Node;

// Função para criar um novo nó
Node* createNode(Rocha rocha) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->rocha = rocha;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Função para inserir uma nova rocha na árvore
Node* insert(Node* root, Rocha rocha) {
    if (root == NULL) {
        return createNode(rocha);
    }
    if (strcmp(rocha.nome, root->rocha.nome) < 0) {
        root->left = insert(root->left, rocha);
    } else if (strcmp(rocha.nome, root->rocha.nome) > 0) {
        root->right = insert(root->right, rocha);
    }
    return root;
}

// Função para buscar uma rocha na árvore pelo nome
Node* search(Node* root, char* nome) {
    if (root == NULL || strcmp(root->rocha.nome, nome) == 0) {
        return root;
    }
    if (strcmp(nome, root->rocha.nome) < 0) {
        return search(root->left, nome);
    } else {
        return search(root->right, nome);
    }
}

// Função para encontrar o nó mínimo na árvore
Node* findMin(Node* root) {
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

// Função para remover uma rocha da árvore
Node* removeNode(Node* root, Rocha rocha, int* removed) {
    if (root == NULL) {
        return NULL;
    }
    if (strcmp(rocha.nome, root->rocha.nome) < 0) {
        root->left = removeNode(root->left, rocha, removed);
    } else if (strcmp(rocha.nome, root->rocha.nome) > 0) {
        root->right = removeNode(root->right, rocha, removed);
    } else {
        if (strcmp(rocha.tipo, root->rocha.tipo) != 0) {
            *removed = 0;
            return root;
        }

        *removed = 1;
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
        root->rocha = temp->rocha;
        root->right = removeNode(root->right, temp->rocha, removed);
    }
    return root;
}

// Função para imprimir as informações de uma rocha
void printRocha(Rocha rocha) {
    printf("Nome: %s\n", rocha.nome);
    printf("Tipo: %s\n", rocha.tipo);
}

// Função principal
int main() {
    setlocale(LC_ALL, "");

    Node* root = NULL;
    int opcao;
    
    do {
        scanf("%d", &opcao);
        if (opcao == 1) {
            Rocha rocha;
            getchar(); // Consome o newline após a leitura do inteiro
            fgets(rocha.nome, 100, stdin);
            rocha.nome[strcspn(rocha.nome, "\n")] = '\0'; // Remove o newline do final
            fgets(rocha.tipo, 50, stdin);
            rocha.tipo[strcspn(rocha.tipo, "\n")] = '\0'; // Remove o newline do final
            root = insert(root, rocha);
        } else if (opcao == 2) {
            char nome[100];
            getchar(); // Consome o newline após a leitura do inteiro
            fgets(nome, 100, stdin);
            nome[strcspn(nome, "\n")] = '\0'; // Remove o newline do final
            Node* resultado = search(root, nome);
            if (resultado != NULL) {
                printRocha(resultado->rocha);
            } else {
                printf("Rocha nao encontrada\n");
            }
        } else if (opcao == 3) {
            Rocha rocha;
            getchar(); // Consome o newline após a leitura do inteiro
            fgets(rocha.nome, 100, stdin);
            rocha.nome[strcspn(rocha.nome, "\n")] = '\0'; // Remove o newline do final
            fgets(rocha.tipo, 50, stdin);
            rocha.tipo[strcspn(rocha.tipo, "\n")] = '\0'; // Remove o newline do final
            int removed = 0;
            root = removeNode(root, rocha, &removed);
            if (removed) {
                printf("Rocha removida com sucesso\n");
            } else {
                printf("Rocha nao encontrada para remocao\n");
            }
        } else if (opcao != 0) {
            printf("Operação inválida\n");
        }
    } while (opcao != 0);
    
    return 0;
}
