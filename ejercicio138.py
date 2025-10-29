// Proyecto de Informatica
// Ejercicio 138
Ejercicio 136: Ordenamiento topológico usando Kahn's Algorithm (BFS)
Análisis del Problema
 Ordenar nodos de DAG usando grados de entrada y cola.
Diseño de la Solución
 Contar indegree, agregar a cola los de indegree 0, ir eliminando.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;cin>>n>>m;
    vector<vector<int>> g(n);
    vector<int> indeg(n);
    for(int i=0;i<m;++i){int u,v;cin>>u>>v;g[u].push_back(v);indeg[v]++;}
    queue<int> q;
    for(int i=0;i<n;++i) if(indeg[i]==0) q.push(i);
    vector<int> order;
    while(!q.empty()){
        int u=q.front();q.pop();
        order.push_back(u);
        for(int v:g[u]) if(--indeg[v]==0) q.push(v);
    }
    for(int x:order) cout<<x<<" ";
}

Pruebas
? DAG simple con dependencias produce orden válido.