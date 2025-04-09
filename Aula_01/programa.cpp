#include <iostream>
#include <string>

using namespace std;

int main() {
    string nome;
    int idade;

    cout << "Digite seu nome: ";
    //cin >> nome; lê nome sem espaços
    getline(cin, nome); // Usamos getline para ler a linha inteira, incluindo espaços

    cout << "Digite sua idade: ";
    cin >> idade;

    cout << "Olá, " << nome << "! Você tem " << idade << " anos." << endl;

    return 0;
}