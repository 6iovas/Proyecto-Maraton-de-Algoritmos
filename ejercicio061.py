// Proyecto de Informatica
// Ejercicio 61
Ejercicio 59: Detectar ciclo en grafo dirigido (DFS con estados)
Análisis
 DFS con estados 0=unvisited,1=visiting,2=visited.
Diseño
 Si se llega a un nodo visiting -> ciclo.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
bool dfs(int u, vector<vector<int>>& g, vector<int>& st){
    st[u]=1;
    for(int v: g[u]){
        if(st[v]==1) return true;
        if(st[v]==0 && dfs(v,g,st)) return true;
    }
    st[u]=2; return false;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<int>> g(n);
    for(int i=0;i<m;++i){int u,v;cin>>u>>v; g[u].push_back(v);}
    vector<int> st(n,0);
    bool has=false;
    for(int i=0;i<n;++i) if(st[i]==0) if(dfs(i,g,st)){ has=true; break; }
    cout << (has? "CYCLE\n":"ACYCLIC\n");
    return 0;
}

Pruebas
? Grafo con back edge ? CYCLE.