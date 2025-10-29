// Proyecto de Informatica
// Ejercicio 244
Ejercicio 26  IDA* (Iterative Deepening A*) aplicado al puzzle 8 (3x3)  heurística Manhattan
Análisis
 Resolver puzzle 8 (3x3) con IDA*  búsqueda iterativa por profundidad con límite f = g + h, donde h es Manhattan distance heuristic. IDA* es espacio eficiente (DFS with cost bound).
Diseño
? Representar estado como array[9] con 0 = blank.

? Heurística: sum of Manhattan distances of tiles to goal.

? IDA*: incrementar límite desde h(start) hasta solution; DFS prune when g + h > bound.

? Para evitar immediate backtracking, track previous move.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int dx[4]={-1,1,0,0}, dy[4]={0,0,-1,1};
int manhattan(const array<int,9>& s){
    int res=0;
    for(int i=0;i<9;++i){
        int v=s[i];
        if(v==0) continue;
        int gx = (v-1)/3, gy = (v-1)%3;
        int x=i/3, y=i%3;
        res += abs(x-gx)+abs(y-gy);
    }
    return res;
}
bool dfs(array<int,9>& state, int blank, int g, int bound, int prev_move, vector<int>& path){
    int h = manhattan(state);
    int f = g + h;
    if(f > bound) return false;
    if(h==0) return true;
    int x = blank/3, y = blank%3;
    for(int dir=0; dir<4; ++dir){
        if((prev_move^1) == dir) continue; // avoid going back (since dirs paired 0/1,2/3)
        int nx=x+dx[dir], ny=y+dy[dir];
        if(nx<0||ny<0||nx>=3||ny>=3) continue;
        int npos = nx*3+ny;
        swap(state[blank], state[npos]);
        path.push_back(state[blank]); // pushed moved tile value (optional)
        if(dfs(state, npos, g+1, bound, dir, path)) return true;
        path.pop_back();
        swap(state[blank], state