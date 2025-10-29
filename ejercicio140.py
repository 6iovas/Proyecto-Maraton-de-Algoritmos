// Proyecto de Informatica
// Ejercicio 140
Ejercicio 138: Prim (MST) con priority_queue
Análisis del Problema
 Construir un MST desde cualquier nodo usando heap mínimo.
Diseño de la Solución
 Agregar aristas accesibles, tomar la menor no visitada.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;cin>>n>>m;
    vector<vector<pair<int,int>>> g(n);
    for(int i=0;i<m;++i){int u,v,w;cin>>u>>v>>w;g[u].push_back({v,w});g[v].push_back({u,w});}
    vector<int> vis(n);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0,0});
    int total=0;
    while(!pq.empty()){
        auto [w,u]=pq.top();pq.pop();
        if(vis[u])continue;
        vis[u]=1;total+=w;
        for(auto [v,wt]:g[u]) if(!vis[v]) pq.push({wt,v});
    }
    cout<<"Costo MST: "<<total<<"\n";
}