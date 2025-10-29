// Proyecto de Informatica
// Ejercicio 24
Ejercicio 22: Estabilidad  sort vs stable_sort
Análisis
 Demostrar que stable_sort mantiene orden relativo de claves iguales, sort no garantiza.
Diseño
 Crear pares (key, id), ordenar por key, observar id orden.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    vector<pair<int,int>> v = {{2,1},{1,2},{2,3},{1,4},{2,5}};
    auto a = v; // for sort
    auto b = v; // for stable_sort
    sort(a.begin(), a.end(), [](auto &x, auto &y){ return x.first < y.first; });
    stable_sort(b.begin(), b.end(), [](auto &x, auto &y){ return x.first < y.first; });

    cout << "sort:\n";
    for(auto &p:a) cout<<p.first<<','<<p.second<<' ';
    cout<<"\nstable_sort:\n";
    for(auto &p:b) cout<<p.first<<','<<p.second<<' ';
    cout<<"\n";
    return 0;
}

Pruebas
? Observa que stable_sort mantiene id order for equal keys.