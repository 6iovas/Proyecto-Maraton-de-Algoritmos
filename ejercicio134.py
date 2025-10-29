// Proyecto de Informatica
// Ejercicio 134
Ejercicio 132: FloydWarshall (todas las parejas de caminos más cortos)
Análisis del Problema
 Calcular la distancia mínima entre cada par de nodos en un grafo.
Diseño de la Solución
 Usar matriz dist[i][j] y actualizar:
 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m; cin >> n >> m;
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for(int i=0;i<n;++i) dist[i][i]=0;
    for(int i=0;i<m;++i){
        int u,v,w; cin >> u >> v >> w;
        dist[u][v]=w;
    }
    for(int k=0;k<n;++k)
        for(int i=0;i<n;++i)
            for(int j=0;j<n;++j)
                if(dist[i][k]<INF && dist[k][j]<INF)
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
    for(int i=0;i<n;++i){
        for(int j=0;j<n;++j)
            cout << (dist[i][j]==INF? -1 : dist[i][j]) << " ";
        cout << "\n";
    }
}

Pruebas
? Grafo con 4 nodos y aristas dirigidas.