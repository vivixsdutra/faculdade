#include <iostream>
#include <string>

using namespace std;

// Função recursiva para busca binária
int buscaBinaria(string poneglyphs[], int inicio, int fim, string alvo) {
    if (fim >= inicio) {
        int meio = inicio + (fim - inicio) / 2;

        // Se o elemento está presente no meio
        if (poneglyphs[meio] == alvo)
            return meio;

        // Se o elemento está antes do meio
        if (poneglyphs[meio] > alvo)
            return buscaBinaria(poneglyphs, inicio, meio - 1, alvo);

        // Se o elemento está depois do meio
        return buscaBinaria(poneglyphs, meio + 1, fim, alvo);
    }

    // Elemento não encontrado
    return -1;
}

// Função principal para buscar o índice de uma Poneglyph
int buscarPoneglyph(string poneglyphs[], int tamanho, string alvo) {
    return buscaBinaria(poneglyphs, 0, tamanho - 1, alvo);
}

int main() {
	
	setlocale(LC_ALL, "Portuguese");

	
    const int NUM_ILHAS = 8;
    string poneglyphs[NUM_ILHAS];
    
    // Entrada das ilhas
    poneglyphs[0] = "Alabasta";
    poneglyphs[1] = "Dressrosa";
    poneglyphs[2] = "Enies Lobby";
    poneglyphs[3] = "Skypiea";
    poneglyphs[4] = "Thriller Bark";
    poneglyphs[5] = "Wano";
    poneglyphs[6] = "Water 7";
    poneglyphs[7] = "Skypiea"; // Última entrada, considerada a ilha onde as Poneglyphs estão

    // Nome da Poneglyph a ser procurada
    string alvo = "Skypiea";

    // Busca pela Poneglyph
    int indice = buscarPoneglyph(poneglyphs, NUM_ILHAS - 1, alvo);

    if (indice != -1)
        cout << "Índice da pista encontrada: " << indice << endl;

    return 0;
}
