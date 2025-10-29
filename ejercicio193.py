// Proyecto de Informatica
// Ejercicio 193
Ejercicio 189: Merge intervals (unir intervalos solapados)
Análisis
 Dado lista de intervalos [l,r], unir los que se solapan.
Diseño
 Ordenar por inicio y fusionar recorriendo.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<pair<int,int>> a(n);
    for(int i=0;i<n;++i) cin>>a[i].first>>a[i].second;
    sort(a.begin(), a.end());
    vector<pair<int,int>> res;
    for(auto &iv: a){
        if(res.empty() || iv.first > res.back().second) res.push_back(iv);
        else res.back().second = max(res.back().second, iv.second);
    }
    for(auto &p: res) cout<<p.first<<" "<<p.second<<"\n";
}

Prueba
? [[1,3],[2,6],[8,10],[15,18]] ? [1,6] [8,10] [15,18]