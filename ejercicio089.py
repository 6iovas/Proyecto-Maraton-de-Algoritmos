// Proyecto de Informatica
// Ejercicio 89
Título del Ejercicio: Contar Duplicados con multiset
Código Fuente (C++):
#include <iostream>
#include <set>
using namespace std;

int main(){
    int n; cin>>n;
    multiset<int> ms;
    for(int i=0;i<n;i++){ int x; cin>>x; ms.insert(x);}

    cout<<"Elementos y cantidad:\n";
    for(int x:ms) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [1 2 2 3] ? Salida: 1 2 2 3
88. Cola de Prioridad con std::priority_queue