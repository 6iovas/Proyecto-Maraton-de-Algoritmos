// Proyecto de Informatica
// Ejercicio 144
Ejercicio 142: Detectar componentes conexas (DFS)
Análisis del Problema
 Contar cuántas componentes hay en un grafo no dirigido.
Diseño de la Solución
 DFS para marcar visitados y contar cuántas veces se llama desde un nodo no visitado.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> g;
vector<int> vis;
void dfs(int u){vis[u]=1;for(int v:g[u])if(!vis[v])dfs(v);}
int main(){
    int n,m;cin>>n>>m;
    g.resize(n);
    for(int i=0;i<m;++i){int u,v;cin>>u>>v;g[u].push_back(v);g[v].push_back(u);}
    vis.assign(n,0);
    int comps=0;
    for(int i=0;i<n;++i) if(!vis[i]){dfs(i);comps++;}
    cout<<"Componentes: "<<comps<<"\n";
}