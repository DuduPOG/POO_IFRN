#include <iostream>

using namespace std;

int main() {
    
    int x = 0, y = 5, z = 10; //a variável é uma instância do tipo (local da memória que se guarda uma informação)
    int *p=&y;
    p = p + 1;
    int *q = new int;


    cout << x << " | " << &x << endl;
    cout << y << " | " << &y << endl;
    cout << z << " | " << &z << endl;
    cout << p << " | " << &p << endl; //p armazena um endereço da memória e nesse endereço pode ter qualquer coisa, ele é um ponteiro
    cout << q << " | " << &q << endl; //a mesma regra se aplica a q

    /*
    Python
    x=0 a variável é referência para uma instância do tipo
    x=(local da memóra) --> (local da memória)=0
    */

    return 0;
}