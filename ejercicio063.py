// Proyecto de Informatica
// Ejercicio 63
Ejercicio 61: Topological sort (Kahn y DFS)
Análisis
 Orden topológico en DAG.
Diseño
 Implementar Kahn (BFS con indegree).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<int>> g(n);
    vector<int> indeg(n,0);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; g[u].push_back(v); indeg[v]++; }
    queue<int> q;
    for(int i=0;i<n;++i) if(indeg[i]==0) q.push(i);
    vector<int> topo;
    while(!q.empty()){
        int u=q.front(); q.pop();
        topo.push_back(u);
        for(int v: g[u]) if(--indeg[v]==0) q.push(v);
    }
    if((int)topo.size()!=n) { cout<<"CYCLE\n"; return 0; }
    for(int x: topo) cout<<x<<' ';
    cout<<'\n';
    return 0;
}

Pruebas
? DAG -> topo order; ciclo -> imprime CYCLE.