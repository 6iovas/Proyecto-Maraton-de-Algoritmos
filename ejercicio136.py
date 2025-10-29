// Proyecto de Informatica
// Ejercicio 136
Ejercicio 134: Topological Sort con DFS
Análisis del Problema
 Ordenar los vértices de un grafo dirigido acíclico (DAG).
Diseño de la Solución
 Usar DFS con pila de salida.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> g;
vector<int> vis, order;

void dfs(int u){
    vis[u]=1;
    for(int v:g[u]) if(!vis[v]) dfs(v);
    order.push_back(u);
}

int main(){
    int n,m; cin>>n>>m;
    g.resize(n);
    for(int i=0;i<m;++i){int u,v;cin>>u>>v;g[u].push_back(v);}
    vis.assign(n,0);
    for(int i=0;i<n;++i) if(!vis[i]) dfs(i);
    reverse(order.begin(), order.end());
    for(int x:order) cout<<x<<" ";
}

Pruebas
? Entrada: DAG con 6 vértices, imprime orden topológico válido.