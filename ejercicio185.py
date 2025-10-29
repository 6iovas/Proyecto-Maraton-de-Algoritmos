// Proyecto de Informatica
// Ejercicio 185
Ejercicio 181: Minimum number of swaps to sort array
Analisis
 Contar swaps mínimos para ordenar array con elementos únicos.
Diseño
 Use pair (value,index), sort, and count cycles.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<pair<int,int>> a(n);
    for(int i=0;i<n;++i){ cin>>a[i].first; a[i].second = i; }
    sort(a.begin(), a.end());
    vector<char> vis(n,false);
    int ans=0;
    for(int i=0;i<n;++i){
        if(vis[i] || a[i].second==i) continue;
        int cycle=0, j=i;
        while(!vis[j]){ vis[j]=1; j = a[j].second; cycle++; }
        if(cycle>0) ans += cycle-1;
    }
    cout<<ans<<"\n";
}

Prueba
? 4 4 3 2 1 ? swaps 2? Actually for [4,3,2,1] minimal swaps = 2? For unique check: output 2? (works)