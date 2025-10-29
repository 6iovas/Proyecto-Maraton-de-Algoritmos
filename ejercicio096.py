// Proyecto de Informatica
// Ejercicio 96
Título del Ejercicio: Orden Descendente con sort + reverse
Análisis del Problema
? Descripción del Problema: Ordenar un vector de enteros de mayor a menor utilizando std::sort y luego invertir con std::reverse.

? Entradas y Salidas:

? Entrada: Vector de enteros.

? Salida: Vector ordenado descendente.

Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n; cin >> n;
    vector<int> v(n);
    for(int i=0;i<n;i++) cin>>v[i];

    sort(v.begin(),v.end());
    reverse(v.begin(),v.end());

    cout<<"Vector ordenado descendente: ";
    for(int x:v) cout<<x<<" ";
    cout<<endl;
    return 0;
}

Pruebas:
? Caso 1: Entrada [4 1 3 2] ? Salida: 4 3 2 1

95. Ordenar estructuras por nombre usando std::sort