// Proyecto de Informatica
// Ejercicio 135
Ejercicio 133: BellmanFord (detección de ciclos negativos)
Análisis del Problema
 Detectar si un grafo tiene un ciclo de peso negativo y calcular distancias.
Diseño de la Solución
 Relaxar todas las aristas N?1 veces; si en una iteración adicional mejora una distancia, hay ciclo negativo.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

struct Edge { int u,v,w; };

int main(){
    int n,m; cin>>n>>m;
    vector<Edge> edges(m);
    for(auto &e: edges) cin>>e.u>>e.v>>e.w;
    vector<long long> dist(n, 1e18);
    int s; cin>>s;
    dist[s]=0;
    for(int i=0;i<n-1;++i)
        for(auto &e: edges)
            if(dist[e.u]<1e18 && dist[e.v]>dist[e.u]+e.w)
                dist[e.v]=dist[e.u]+e.w;
    bool neg=false;
    for(auto &e: edges)
        if(dist[e.u]<1e18 && dist[e.v]>dist[e.u]+e.w) neg=true;
    cout<<(neg?"CICLO NEGATIVO":"OK")<<"\n";
    for(int i=0;i<n;++i) cout<<dist[i]<<" ";
}

Pruebas
? Grafo sin ciclo ? OK;

? Grafo con ciclo negativo ? CICLO NEGATIVO.