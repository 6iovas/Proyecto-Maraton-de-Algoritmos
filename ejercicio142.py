// Proyecto de Informatica
// Ejercicio 142
Ejercicio 140: FloydWarshall con reconstrucción de camino
Análisis del Problema
 Guardar predecesores para reconstruir el camino mínimo entre dos nodos.
Diseño de la Solución
 Matriz next[i][j] que almacena el siguiente nodo en el camino.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;cin>>n>>m;
    const int INF=1e9;
    vector<vector<int>> dist(n, vector<int>(n,INF)), nxt(n, vector<int>(n,-1));
    for(int i=0;i<n;++i) dist[i][i]=0;
    for(int i=0;i<m;++i){
        int u,v,w;cin>>u>>v>>w;
        dist[u][v]=w; nxt[u][v]=v;
    }
    for(int k=0;k<n;++k)
        for(int i=0;i<n;++i)
            for(int j=0;j<n;++j)
                if(dist[i][k]+dist[k][j]<dist[i][j]){
                    dist[i][j]=dist[i][k]+dist[k][j];
                    nxt[i][j]=nxt[i][k];
                }
    int u,v;cin>>u>>v;
    if(nxt[u][v]==-1){cout<<"No path\n";return 0;}
    vector<int> path={u};
    while(u!=v){u=nxt[u][v];path.push_back(u);}
    for(int x:path) cout<<x<<" ";
}