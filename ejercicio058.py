// Proyecto de Informatica
// Ejercicio 58
Ejercicio 56: Dijkstra (grafo ponderado con pesos no negativos)
Análisis
 Encontrar distancias mínimas desde s.
Diseño
 Min-heap PQ.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL<<60);
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<pair<int,ll>>> g(n);
    for(int i=0;i<m;++i){ int u,v; ll w; cin>>u>>v>>w; g[u].push_back({v,w}); g[v].push_back({u,w}); }
    int s; cin>>s;
    vector<ll> dist(n, INF);
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
    dist[s]=0; pq.push({0,s});
    while(!pq.empty()){
        auto [d,u]=pq.top(); pq.pop();
        if(d!=dist[u]) continue;
        for(auto [v,w]: g[u]) if(dist[v] > d+w){ dist[v] = d+w; pq.push({dist[v], v}); }
    }
    for(int i=0;i<n;++i) cout << (dist[i]==INF ? -1 : dist[i]) << (i+1==n?'\n':' ');
    return 0;
}

Pruebas
? Probar con un pequeño grafo con pesos.