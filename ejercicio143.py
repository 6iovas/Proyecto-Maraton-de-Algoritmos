// Proyecto de Informatica
// Ejercicio 143
Ejercicio 141: Camino más corto con obstáculos (BFS en matriz)
Análisis del Problema
 Encontrar la distancia mínima en una cuadrícula con celdas bloqueadas.
Diseño de la Solución
 BFS con movimientos 4-direccionales validando límites y obstáculos.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;cin>>n>>m;
    vector<string> grid(n);
    for(auto &s:grid)cin>>s;
    int sx,sy,ex,ey;cin>>sx>>sy>>ex>>ey;
    vector<vector<int>> dist(n,vector<int>(m,-1));
    queue<pair<int,int>> q;
    q.push({sx,sy});
    dist[sx][sy]=0;
    int dx[4]={1,-1,0,0}, dy[4]={0,0,1,-1};
    while(!q.empty()){
        auto [x,y]=q.front();q.pop();
        for(int i=0;i<4;++i){
            int nx=x+dx[i], ny=y+dy[i];
            if(nx<0||ny<0||nx>=n||ny>=m||grid[nx][ny]=='#'||dist[nx][ny]!=-1) continue;
            dist[nx][ny]=dist[x][y]+1;
            q.push({nx,ny});
        }
    }
    cout<<dist[ex][ey]<<"\n";
}