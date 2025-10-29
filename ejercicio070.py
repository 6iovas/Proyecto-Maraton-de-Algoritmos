// Proyecto de Informatica
// Ejercicio 70
Ejercicio 68: Puentes y puntos de articulación (Tarjan)
Análisis
 Detectar bridges and articulation points.
Diseño
 DFS time & low arrays.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
void dfs(int u,int p, vector<vector<int>>& g, vector<int>& tin, vector<int>& low, vector<char>& vis, int &t, vector<pair<int,int>>& bridges){
    vis[u]=1; tin[u]=low[u]=t++;
    for(int v: g[u]){
        if(v==p) continue;
        if(vis[v]) low[u]=min(low[u], tin[v]);
        else {
            dfs(v,u,g,tin,low,vis,t,bridges);
            low[u]=min(low[u], low[v]);
            if(low[v] > tin[u]) bridges.emplace_back(u,v);
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<int>> g(n);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; g[u].push_back(v); g[v].push_back(u); }
    vector<int> tin(n,-1), low(n,-1); vector<char> vis(n,0);
    int timer=0; vector<pair<int,int>> bridges;
    for(int i=0;i<n;++i) if(!vis[i]) dfs(i,-1,g,tin,low,vis,timer,bridges);
    for(auto &e: bridges) cout<<e.first<<" "<<e.second<<"\n";
    return 0;
}

Pruebas
? Grafo con bridge edges detectados listados.