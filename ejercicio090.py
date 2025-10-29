// Proyecto de Informatica
// Ejercicio 90
Título del Ejercicio: Priority Queue
Código Fuente (C++):
#include <iostream>
#include <queue>
using namespace std;

int main(){
    priority_queue<int> pq;
    int n; cin>>n;
    for(int i=0;i<n;i++){ int x; cin>>x; pq.push(x);}

    cout<<"Elementos en orden de prioridad: ";
    while(!pq.empty()){ cout<<pq.top()<<" "; pq.pop();}
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [3 1 5] ? Salida: 5 3 1

89. Contar palabras más frecuentes con std::unordered_map