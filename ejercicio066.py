// Proyecto de Informatica
// Ejercicio 66
Ejercicio 64: Prim  Minimum Spanning Tree (heap implementation)
Análisis
 MST por Prim con PQ.
Diseño
 Start at node 0, push edges, pick min edge connecting new vertex.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<pair<int,ll>>> g(n);
    for(int i=0;i<m;++i){ int u,v; ll w; cin>>u>>v>>w; g[u].push_back({v,w}); g[v].push_back({u,w}); }
    vector<char> used(n,0);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
    used[0]=1;
    for(auto &e: g[0]) pq.push({e.second, e.first});
    ll total=0; int cnt=1;
    while(!pq.empty() && cnt<n){
        auto [w,u]=pq.top(); pq.pop();
        if(used[u]) continue;
        used[u]=1; total+=w; cnt++;
        for(auto &e: g[u]) if(!used[e.first]) pq.push({e.second, e.first});
    }
    if(cnt<n) cout<<"NO MST\n"; else cout<<total<<"\n";
    return 0;
}

Pruebas
? Ejemplo simple MST check.