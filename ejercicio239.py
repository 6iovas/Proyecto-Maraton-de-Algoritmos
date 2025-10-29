// Proyecto de Informatica
// Ejercicio 239
Ejercicio 21  Min-Cost Max-Flow (SPFA + potentials / successive shortest augmenting path)
Análisis
 Dado un grafo dirigido con capacidades y costos en aristas, encontrar el flujo máximo de costo mínimo entre s y t (o bien flujo de tamaño F con coste mínimo). Implementaremos la versión que encuentra flujo máximo con coste mínimo (aumenta hasta que no haya más camino con capacidad). Debe manejar costos negativos (sin ciclos negativos en capacidad residual al inicio) y funcionar con eficiencia suficiente para grafos de tamaño moderado.
Diseño
? Representación con aristas to, rev, cap, cost.

? Usar SPFA (o Dijkstra con potentials) para obtener camino de coste mínimo en el residual graph; preferible Dijkstra con potentials para eficiencia: mantener pot[] (Johnson trick) para convertir costes no negativos.

? Repetir hasta que no haya camino con capacidad.

? Complejidad: cada augment con Dijkstra O(m log n).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct Edge { int to, rev; int cap; long long cost; };
struct MCMF {
    int n;
    vector<vector<Edge>> g;
    MCMF(int n): n(n), g(n) {}
    void addEdge(int u,int v,int cap,long long cost){
        g[u].push_back({v, (int)g[v].size(), cap, cost});
        g[v].push_back({u, (int)g[u].size()-1, 0, -cost});
    }
    // returns {flow, cost}
    pair<int,long long> minCostMaxFlow(int s,int t){
        int flow=0; long long cost=0;
        const long long INFLL = (1LL<<60);
        vector<long long> pot(n,0), dist(n);
        vector<int> pv(n), pe(n);
        // initial potentials (0) is fine if no negative cycles
        while(true){
            // Dijkstra
            priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
            fill(dist.begin(), dist.end(), INFLL);
            dist[s]=0; pq.push({0,s});
            while(!pq.empty()){
                auto [d,u]=pq.top(); pq.pop();
                if(d!=dist[u]) continue;
                for(int i=0;i<(int)g[u].size();++i){
                    Edge &e = g[u][i];
                    if(e.cap<=0) continue;
                    long long nd = d + e.cost + pot[u] - pot[e.to];
                    if(nd < dist[e.to]){
                        dist[e.to]=nd; pv[e.to]=u; pe[e.to]=i;
                        pq.push({nd,e.to});
                    }
                }
            }
            if(dist[t]==INFLL) break;
            for(int i=0;i<n;++i) if(dist[i]<INFLL) pot[i]+=dist[i];
            // augment
            int add = INT_MAX;
            for(int v=t; v!=s; v=pv[v]) add = min(add, g[pv[v]][pe[v]].cap);
            for(int v=t; v!=s; v=pv[v]){
                Edge &e = g[pv[v]][pe[v]];
                e.cap -= add;
                g[v][e.rev].cap += add;
            }
            flow += add;
            cost += (long long)add * pot[t];
        }
        return {flow, cost};
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Example input:
    // n m
    // m lines: u v cap cost
    // s t
    int n,m; if(!(cin>>n>>m)) return 0;
    MCMF mcmf(n);
    for(int i=0;i<m;++i){
        int u,v,cap; long long cost;
        cin>>u>>v>>cap>>cost;
        mcmf.addEdge(u,v,cap,cost);
    }
    int s,t; cin>>s>>t;
    auto res = mcmf.minCostMaxFlow(s,t);
    cout<<"MaxFlow="<<res.first<<" MinCost="<<res.second<<"\n";
    return 0;
}

Pruebas
Grafo pequeño con 4 nodos:

 n=4 m=5
0 1 2 1
0 2 1 2
1 2 1 0
1 3 1 3
2 3 2 1
s=0 t=3
?  Resultado esperado: flujo máximo 3 con coste mínimo (verificar salida).