// Proyecto de Informatica
// Ejercicio 60
Ejercicio 58: Floyd-Warshall (All-pairs shortest paths)
Análisis
 Todas las parejas, matriz de distancias.
Diseño
 DP 3-bucle dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 1e15;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<ll>> dist(n, vector<ll>(n, INF));
    for(int i=0;i<n;++i) dist[i][i]=0;
    for(int i=0;i<m;++i){ int u,v; ll w; cin>>u>>v>>w; dist[u][v]=min(dist[u][v], w); }
    for(int k=0;k<n;++k) for(int i=0;i<n;++i) for(int j=0;j<n;++j)
        if(dist[i][k]<INF && dist[k][j]<INF) dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j]);
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j) cout << (dist[i][j]==INF? -1 : dist[i][j]) << (j+1==n?'\n':' ');
    }
    return 0;
}

Pruebas
? Pequeña matriz con pesos y ver resultados.