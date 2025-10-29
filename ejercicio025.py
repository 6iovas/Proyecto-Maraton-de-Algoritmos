// Proyecto de Informatica
// Ejercicio 25
Ejercicio 23: Comparator con lambda que captura variables
Análisis
 Ordenar vectores según una clave externa (p. ej. prioridad dada en map).
Diseño
 Crear map<int,int> priority y lambda captura por referencia.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> v = {5,2,7,3,9};
    unordered_map<int,int> pr = {{5,1},{2,3},{7,2},{3,5},{9,4}};
    sort(v.begin(), v.end(), [&](int a, int b){
        return pr[a] < pr[b]; // orden según prioridad (menor mejor)
    });
    for(int x:v) cout<<x<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? Salida depende de pr map ordering.