// Proyecto de Informatica
// Ejercicio 30
Ejercicio 28: Ordenar vector de pares por (first, second)
Análisis
 Orden lexicográfico simple de pairs.
Diseño
 std::sort funciona directamente para pair<int,int>.
Código
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<pair<int,int>> v(n);
    for(int i=0;i<n;++i) cin>>v[i].first>>v[i].second;
    sort(v.begin(), v.end()); // by first then second
    for(auto &p: v) cout<<p.first<<','<<p.second<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? [(2,3),(1,4),(2,1)] ? (1,4) (2,1) (2,3).