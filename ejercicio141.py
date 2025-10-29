// Proyecto de Informatica
// Ejercicio 141
Ejercicio 139: Caminos más cortos con BFS en grafo no ponderado
Análisis del Problema
 Calcular distancias mínimas (en número de aristas) desde un nodo fuente.
Diseño de la Solución
 Usar cola (queue) BFS tradicional.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;cin>>n>>m;
    vector<vector<int>> g(n);
    for(int i=0;i<m;++i){int u,v;cin>>u>>v;g[u].push_back(v);g[v].push_back(u);}
    int s;cin>>s;
    vector<int> dist(n,-1);
    queue<int> q;q.push(s);dist[s]=0;
    while(!q.empty()){
        int u=q.front();q.pop();
        for(int v:g[u]) if(dist[v]==-1){
            dist[v]=dist[u]+1;
            q.push(v);
        }
    }
    for(int i=0;i<n;++i) cout<<dist[i]<<" ";
}