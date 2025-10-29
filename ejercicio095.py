// Proyecto de Informatica
// Ejercicio 95
Título del Ejercicio: Operaciones de Cola
Código Fuente (C++):
#include <iostream>
#include <queue>
using namespace std;

int main(){
    queue<int> q;
    int n; cin>>n;
    for(int i=0;i<n;i++){ int x; cin>>x; q.push(x);}

    cout<<"Sacando elementos de la cola: ";
    while(!q.empty()){ cout<<q.front()<<" "; q.pop();}
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [1 2 3] ? Salida: 1 2 3
94. Ordenar un vector de enteros usando std::reverse después de std::sort