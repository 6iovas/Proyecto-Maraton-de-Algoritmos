// Proyecto de Informatica
// Ejercicio 68
Ejercicio 66: Hopcroft-Karp (matching máximo bipartito)  esquema básico
Análisis
 Emparejamiento máximo en grafo bipartito, implementación Hopcroft-Karp.
Diseño
 BFS para dist levels + DFS to find augmenting paths.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
struct HopcroftKarp {
    int nL, nR; vector<vector<int>> adj; vector<int> dist, pairU, pairV;
    HopcroftKarp(int nL,int nR):nL(nL),nR(nR),adj(nL),pairU(nL,-1),pairV(nR,-1),dist(nL){}
    void addEdge(int u,int v){ adj[u].push_back(v); }
    bool bfs(){
        queue<int> q;
        for(int u=0;u<nL;++u){
            if(pairU[u]==-1){ dist[u]=0; q.push(u); }
            else dist[u]=INT_MAX;
        }
        bool reachable=false;
        while(!q.empty()){
            int u=q.front(); q.pop();
            for(int v: adj[u]){
                if(pairV[v]!=-1 && dist[pairV[v]]==INT_MAX){
                    dist[pairV[v]] = dist[u]+1; q.push(pairV[v]);
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
        dist[u]=INT_MAX; return false;
    }
    int maxMatching(){
        int result=0;
        while(bfs()){
            for(int u=0;u<nL;++u) if(pairU[u]==-1 && dfs(u)) ++result;
        }
        return result;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int nL,nR,m; if(!(cin>>nL>>nR>>m)) return 0;
    HopcroftKarp hk(nL,nR);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; hk.addEdge(u,v); }
    cout<<hk.maxMatching()<<"\n";
    return 0;
}

Pruebas
? Validar en bipartite graphs.