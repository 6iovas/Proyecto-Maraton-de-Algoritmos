// Proyecto de Informatica
// Ejercicio 251
Ejercicio 31  All-Pairs Shortest Paths with Johnson (Dijkstra + reweight)
Análisis
 Calcular distancias mínimas entre todos los pares en grafo dirigido con pesos (puede tener aristas negativas, pero sin ciclos negativos). FloydWarshall es O(n³); Johnson usa una corrida de BellmanFord una vez y luego Dijkstra desde cada nodo: O(n m log n) ideal para grafos esparsos.
Diseño
1. Añadir nodo ficticio s' con aristas 0 a todos.

2. Ejecutar BellmanFord desde s' para obtener potencias h[v]; si detecta ciclo negativo -> abortar.

3. Reweight edges: w'(u,v) = w(u,v) + h[u] - h[v] (no-negativos).

4. Ejecutar Dijkstra desde cada nodo con pesos w' y corregir distancias: dist(u,v) = d'(u,v) - h[u] + h[v].

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL<<60);

struct Edge { int u,v; ll w; };

vector<ll> bellmanFord(int n, int s, const vector<Edge>& edges){
    vector<ll> d(n, INF); d[s]=0;
    for(int it=0; it<n-1; ++it){
        bool changed=false;
        for(auto &e: edges) if(d[e.u]<INF && d[e.v] > d[e.u] + e.w){
            d[e.v] = d[e.u] + e.w; changed=true;
        }
        if(!changed) break;
    }
    // check negative cycle
    for(auto &e: edges) if(d[e.u]<INF && d[e.v] > d[e.u] + e.w) return {};
    return d;
}

vector<ll> dijkstra(int n, int s, const vector<vector<pair<int,ll>>>& g){
    vector<ll> d(n, INF); d[s]=0;
    priority_queue<pair<ll,int>, vector<pair<ll,int>>, greater<>> pq;
    pq.push({0,s});
    while(!pq.empty()){
        auto [dist,u] = pq.top(); pq.pop();
        if(dist != d[u]) continue;
        for(auto &ed: g[u]){
            int v = ed.first; ll w = ed.second;
            if(d[v] > d[u] + w){ d[v] = d[u] + w; pq.push({d[v], v}); }
        }
    }
    return d;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<Edge> edges;
    vector<vector<pair<int,ll>>> g(n);
    for(int i=0;i<m;++i){ int u,v; ll w; cin>>u>>v>>w; edges.push_back({u,v,w}); g[u].push_back({v,w}); }
    // Bellman-Ford from artificial node n
    vector<Edge> edges2 = edges;
    for(int v=0; v<n; ++v) edges2.push_back({n, v, 0});
    auto h = bellmanFord(n+1, n, edges2);
    if(h.empty()){ cout<<"Negative cycle detected\n"; return 0; }
    h.resize(n); // drop artificial
    // reweight graph
    vector<vector<pair<int,ll>>> g2(n);
    for(auto &e: edges){
        ll wprime = e.w + h[e.u] - h[e.v];
        if(wprime < 0) wprime = 0; // numeric safety
        g2[e.u].push_back({e.v, wprime});
    }
    // run Dijkstra from each node and adjust distances
    vector<vector<ll>> all(n, vector<ll>(n, INF));
    for(int u=0; u<n; ++u){
        auto d = dijkstra(n, u, g2);
        for(int v=0; v<n; ++v) if(d[v]<INF) all[u][v] = d[v] - h[u] + h[v];
    }
    // output matrix
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j){
            if(all[i][j]>=INF/2) cout<<"INF ";
            else cout<<all[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}

Prueba
? Grafo con 4 nodos y algunas aristas con negativos pero sin ciclos negativos; comparar con FloydWarshall.