// Proyecto de Informatica
// Ejercicio 115
Ejercicio 113: Sort indices usando comparador que usa datos externos
Análisis del Problema
 Ordenar índices 0..n-1 de acuerdo con valores en vector externo key[], sin mover key (orden indirecto).
Diseño de la Solución
 Crear vector de índices y usar sort con lambda que compara key[i].
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> key(n);
    for(int i=0;i<n;++i) cin>>key[i];
    vector<int> idx(n);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), [&](int a, int b){
        if(key[a] != key[b]) return key[a] < key[b];
        return a < b; // tie-breaker stable by index
    });
    for(int i: idx) cout<<i<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? key = [30,10,20] ? idx order 1 2 0.