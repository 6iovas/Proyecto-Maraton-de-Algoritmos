// Proyecto de Informatica
// Ejercicio 210
Ejercicio 5  Shortest path con A* (heurística euclidiana) en grid con obstáculos
Análisis del problema
 Implementar A* para encontrar camino mínimo (en número de movimientos) en una cuadrícula R x C con obstáculos (#) entre start (sx,sy) y goal (gx,gy). Usar heurística Euclidiana (o Manhattan si movimiento 4-dir). Demostrar que para 4-direcciones Manhattan es admissible.
Diseño de la solución
? Representar grid, vecinos 4-direccionales.

? g = distancia desde start; h = Manhattan distance to goal; f = g + h.

? Mantener open como priority_queue por menor f (si empate, menor g o por tie-break).

? came_from para reconstruir ruta.

? Complejidad: en práctica, similar a BFS pero visita menos nodos si heurística efectiva.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using pii = pair<int,int>;
struct Node {
    int f, g;
    int x, y;
    bool operator<(const Node& other) const {
        if (f != other.f) return f > other.f; // min-heap via reversed comparator
        return g < other.g;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int R,C; if(!(cin>>R>>C)) return 0;
    vector<string> grid(R);
    for(int i=0;i<R;++i) cin>>grid[i];
    int sx, sy, gx, gy; cin>>sx>>sy>>gx>>gy; // zero-based coords
    auto h = [&](int x,int y){ return abs(x-gx)+abs(y-gy); }; // Manhattan (admissible)
    const int INF = 1e9;
    vector<vector<int>> g(R, vector<int>(C, INF));
    vector<vector<pii>> parent(R, vector<pii>(C, {-1,-1}));
    priority_queue<Node> open;
    g[sx][sy]=0;
    open.push({h(sx,sy), 0, sx, sy});
    int dx[4]={1,-1,0,0}, dy[4]={0,0,1,-1};

    bool found=false;
    while(!open.empty()){
        Node cur = open.top(); open.pop();
        if (cur.x==gx && cur.y==gy){ found=true; break; }
        if (cur.g != g[cur.x][cur.y]) continue; // outdated
        for(int k=0;k<4;++k){
            int nx=cur.x+dx[k], ny=cur.y+dy[k];
            if(nx<0||ny<0||nx>=R||ny>=C) continue;
            if(grid[nx][ny]=='#') continue;
            int ng = cur.g + 1;
            if(ng < g[nx][ny]){
                g[nx][ny] = ng;
                parent[nx][ny] = {cur.x, cur.y};
                open.push({ng + h(nx,ny), ng, nx, ny});
            }
        }
    }
    if(!found){ cout << "NO PATH\n"; return 0; }
    vector<pii> path;
    for(pii at = {gx,gy}; at.first!=-1; at = parent[at.first][at.second]) path.push_back(at);
    reverse(path.begin(), path.end());
    cout << "Length: " << path.size()-1 << "\n";
    for(auto &p: path) cout << p.first << ' ' << p.second << '\n';
    return 0;
}

Pruebas
? Grid 5x5 with obstacles; test start/goal reachable and unreachable. A* debe producir ruta óptima en número de pasos (por la heurística admisible).