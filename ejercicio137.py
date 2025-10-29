// Proyecto de Informatica
// Ejercicio 137
Ejercicio 135: Detectar ciclo en grafo dirigido (DFS con pila de recursion)
Análisis del Problema
 Verificar si un grafo dirigido contiene un ciclo.
Diseño de la Solución
 DFS con colores (0=no visitado,1=visitando,2=visitado).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> g;
vector<int> state;
bool has_cycle=false;

void dfs(int u){
    state[u]=1;
    for(int v:g[u]){
        if(state[v]==0) dfs(v);
        else if(state[v]==1) has_cycle=true;
    }
    state[u]=2;
}

int main(){
    int n,m;cin>>n>>m;
    g.resize(n);
    for(int i=0;i<m;++i){int u,v;cin>>u>>v;g[u].push_back(v);}
    state.assign(n,0);
    for(int i=0;i<n;++i) if(!state[i]) dfs(i);
    cout<<(has_cycle?"CICLO":"NO CICLO")<<"\n";
}

Pruebas
? Ciclo 0?1?2?0 ? CICLO.