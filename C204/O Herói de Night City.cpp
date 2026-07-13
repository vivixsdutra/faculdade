#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Definindo a struct para representar um implante cibernético
struct Implante {
    string nome;
    string fabricante;
    int tier;
    float taxa_psicose;
};

int main() {
    int N;
    
    cin >> N;

    // Vetor dinâmico para armazenar os implantes
    vector<Implante> implantes(N);

    // Leitura dos dados dos implantes e inserção no vetor
    for (int i = 0; i < N; ++i) {
        cin >> implantes[i].nome;
       
        cin >> implantes[i].fabricante;
        
        cin >> implantes[i].tier;
        
        cin >> implantes[i].taxa_psicose;
    }

    // Verificação da soma das taxas de psicose
    float soma_psicose = 0.0;
    for (int i = 0; i < N; ++i) {
        soma_psicose += implantes[i].taxa_psicose;
    }

    // Verificando se a soma ultrapassa o limite de psicose
    if (soma_psicose > 60.0) {
        cout << "Alerta! Uma recompensa de 50.000 edinhos foi colocada pela sua cabeça. Você se tornou um Ciberpsicopata" << endl;
    } else {
        cout << "Vamos tchum! Temos uma cidade pra conquistar!" << endl;
    }

    return 0;
}
