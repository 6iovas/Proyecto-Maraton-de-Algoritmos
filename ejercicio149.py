// Proyecto de Informatica
// Ejercicio 149
Ejercicio 147: Encontrar subarray con suma máxima (Kadanes Algorithm)
Análisis del Problema
 Dado un vector de enteros (pueden ser negativos), hallar el subarray con la mayor suma posible.
Diseño de la Solución
 Usar Kadane: recorrer el arreglo acumulando suma, reiniciando si la suma cae por debajo de cero.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    vector<int> v(n);
    for(int i=0;i<n;++i) cin >> v[i];
    int best=v[0], curr=0;
    for(int x:v){
        curr = max(x, curr+x);
        best = max(best, curr);
    }
    cout << "Suma máxima: " << best << '\n';
}

Pruebas
? Entrada: 8\n-2 1 -3 4 -1 2 1 -5 4

? Salida: Suma máxima: 6 (subarray [4,-1,2,1])