// Proyecto de Informatica
// Ejercicio 221
Ejercicio 16  HopcroftKarp (Matching máximo en bipartito), implementación completa
Análisis del problema
 Implementar HopcroftKarp para obtener matching máximo en un grafo bipartito (nL left nodes, nR right nodes, m aristas). Debe ser O(E sqrt(V)) en práctica. Devolver tamaño matching y pares.
Diseño de la solución
? Mantener arrays pairU, pairV, dist.

? BFS para construir niveles (distances) desde libres en U.

? DFS para encontrar augmenting paths respectando levels.

? Repetir hasta no encontrar más.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct HopcroftKarp {
    int nL, nR;
    vector<vector<int>> adj;
    vector<int> pairU, pairV, dist;
    const int INF = 1e9;
    HopcroftKarp(int nL, int nR): nL(nL), nR(nR), adj(nL), pairU(nL, -1), pairV(nR, -1), dist(nL) {}
    void addEdge(int u,int v){ adj[u].push_back(v); }
    bool bfs(){
        queue<int> q;
        for(int u=0;u<nL;++u){
            if(pairU[u]==-1){ dist[u]=0; q.push(u); }
            else dist[u]=INF;
        }
        bool reachable=false;
        while(!q.empty()){
            int u=q.front(); q.pop();
            for(int v: adj[u]){
                if(pairV[v]!=-1 && dist[pairV[v]]==INF){
                    dist[pairV[v]] = dist[u]+1;
                    q.push(pairV[v]);
                }
                if(pairV[v]==-1) reachable=true;
            }
        }
        return reachable;
    }
    bool dfs(int u){
        for(int v: adj[u]){
            if(pairV[v]==-1 || (dist[pairV[v]]==dist[u]+1 && dfs(pairV[v]))){
                pairU[u]=v; pairV[v]=u; return true;
            }
        }
        dist[u]=INF; return false;
    }
    int maxMatching(){
        int matching=0;
        while(bfs()){
            for(int u=0;u<nL;++u)
                if(pairU[u]==-1 && dfs(u)) ++matching;
        }
        return matching;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int nL,nR,m; if(!(cin>>nL>>nR>>m)) return 0;
    HopcroftKarp hk(nL,nR);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; hk.addEdge(u,v); }
    int res = hk.maxMatching();
    cout<<"Matching size: "<<res<<"\n";
    for(int u=0;u<nL;++u) if(hk.pairU[u]!=-1) cout<<u<<" - "<<hk.pairU[u]<<"\n";
    return 0;
}

Prueba
? Grafo bipartito: left 3, right 3, edges (0-0),(0-1),(1-1),(2-2) ? matching size 3 (perfect if possible).