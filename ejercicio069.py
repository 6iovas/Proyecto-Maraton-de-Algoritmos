// Proyecto de Informatica
// Ejercicio 69
Ejercicio 67: Contar componentes conectadas (BFS/DFS)
Análisis
 Contar componentes en grafo no dirigido.
Diseño
 DFS/BFS through all nodes marking visited.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<int>> g(n);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; g[u].push_back(v); g[v].push_back(u); }
    vector<char> vis(n,0);
    int comps=0;
    for(int i=0;i<n;++i){
        if(vis[i]) continue;
        comps++;
        queue<int> q; q.push(i); vis[i]=1;
        while(!q.empty()){
            int u=q.front(); q.pop();
            for(int v:g[u]) if(!vis[v]){ vis[v]=1; q.push(v); }
        }
    }
    cout<<comps<<"\n";
    return 0;
}

Pruebas
? Grafo con dos componentes ? 2.