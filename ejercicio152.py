// Proyecto de Informatica
// Ejercicio 152
Ejercicio 150: Rotar un vector k posiciones a la derecha
Análisis del Problema
 Desplazar todos los elementos de un vector hacia la derecha k posiciones.
Diseño de la Solución
 Usar std::rotate o reversas parciales:
1. Invertir todo.

2. Invertir primeros k.

3. Invertir los restantes.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,k; cin>>n>>k;
    vector<int> v(n);
    for(int i=0;i<n;++i) cin>>v[i];
    k %= n;
    reverse(v.begin(),v.end());
    reverse(v.begin(),v.begin()+k);
    reverse(v.begin()+k,v.end());
    for(int x:v) cout<<x<<" ";
}

Pruebas
? Entrada: 5\n1 2 3 4 5\n2

? Salida: 4 5 1 2 3