// Proyecto de Informatica
// Ejercicio 194
Ejercicio 190: Insert interval (insertar y fusionar)
Análisis
 Insertar nuevo intervalo en lista ordenada y fusionar solapamientos.
Diseño
 Recolectar menores, fusionar, luego mayores.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<pair<int,int>> a(n);
    for(int i=0;i<n;++i) cin>>a[i].first>>a[i].second;
    pair<int,int> newI; cin>>newI.first>>newI.second;
    vector<pair<int,int>> res;
    int i=0;
    while(i<n && a[i].second < newI.first) res.push_back(a[i++]);
    while(i<n && a[i].first <= newI.second){
        newI.first = min(newI.first, a[i].first);
        newI.second = max(newI.second, a[i].second);
        ++i;
    }
    res.push_back(newI);
    while(i<n) res.push_back(a[i++]);
    for(auto &p: res) cout<<p.first<<" "<<p.second<<"\n";
}

Prueba
? a=[[1,3],[6,9]] new=[2,5] ? [1,5] [6,9]