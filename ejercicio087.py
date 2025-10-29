// Proyecto de Informatica
// Ejercicio 87
Título del Ejercicio: Insertar y Eliminar en Set
Análisis del Problema
? Descripción del Problema: Insertar y eliminar elementos de un std::set y mostrar resultados.

? Entradas y Salidas:

? Entrada: Lista de elementos a insertar, lista de elementos a eliminar.

? Salida: Set final ordenado.

Código Fuente (C++):
#include <iostream>
#include <set>
using namespace std;

int main(){
    set<int> s;
    int n,m;
    cout<<"Número de elementos a insertar: "; cin>>n;
    cout<<"Ingrese elementos:\n";
    for(int i=0;i<n;i++){ int x; cin>>x; s.insert(x);}
    
    cout<<"Número de elementos a eliminar: "; cin>>m;
    cout<<"Ingrese elementos a eliminar:\n";
    for(int i=0;i<m;i++){ int x; cin>>x; s.erase(x);}
    
    cout<<"Set final: ";
    for(int x:s) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: Insertar [1 2 3], eliminar [2] ? Salida: 1 3

86. Ordenar objetos complejos en std::vector