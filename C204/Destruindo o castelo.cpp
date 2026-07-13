#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Função recursiva com memoização para encontrar o máximo poder de destruição
int knapsack(int idx, int capacidade, const vector<pair<int, int>>& projeteis, vector<vector<int>>& memo) {
    // Caso base: se não há mais projéteis ou a capacidade é zero
    if (idx < 0 || capacidade == 0) {
        return 0;
    }

    // Verificar se o resultado já está na tabela de memoização
    if (memo[idx][capacidade] != -1) {
        return memo[idx][capacidade];
    }

    int poder = projeteis[idx].first;
    int peso = projeteis[idx].second;

    // Se o peso do projétil é maior que a capacidade restante, não o incluímos
    if (peso > capacidade) {
        memo[idx][capacidade] = knapsack(idx - 1, capacidade, projeteis, memo);
    } else {
        // Considerar dois casos: incluir ou não o projétil
        int incluir = poder + knapsack(idx - 1, capacidade - peso, projeteis, memo);
        int nao_incluir = knapsack(idx - 1, capacidade, projeteis, memo);
        memo[idx][capacidade] = max(incluir, nao_incluir);
    }

    return memo[idx][capacidade];
}

string resolver_caso(int N, const vector<pair<int, int>>& projeteis, int K, int R) {
    // Inicializar a tabela de memoização com -1
    vector<vector<int>> memo(N, vector<int>(K + 1, -1));

    // Obter o poder de destruição máximo possível
    int max_destruicao = knapsack(N - 1, K, projeteis, memo);

    // Verificar se a missão foi completada com sucesso
    if (max_destruicao >= R) {
        return "Missao completada com sucesso";
    } else {
        return "Falha na missao";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<pair<int, int>> projeteis(N);
        for (int i = 0; i < N; ++i) {
            int X, Y;
            cin >> X >> Y;
            projeteis[i] = {X, Y};
        }

        int K, R;
        cin >> K >> R;

        cout << resolver_caso(N, projeteis, K, R) << endl;
    }

    return 0;
}
