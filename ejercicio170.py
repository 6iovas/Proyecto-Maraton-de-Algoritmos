// Proyecto de Informatica
// Ejercicio 170
Ejercicio 166: Two-sum usando hash (devolver índices)
Análisis
 Encontrar dos índices con suma X (no ordenado).
Diseño
 Recorrido con unordered_map de valor?índice.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<int>a(n); for(int i=0;i<n;++i)cin>>a[i];
    int X; cin>>X;
    unordered_map<int,int> mp;
    for(int i=0;i<n;++i){
        int need = X - a[i];
        if(mp.count(need)){ cout<<mp[need]<<" "<<i<<"\n"; return 0; }
        mp[a[i]] = i;
    }
    cout<<"NO\n";
}

Prueba
? Entrada: 5 2 7 11 15 1 9 (n=5 array then X=9) ? Salida: 0 1 (2+7)