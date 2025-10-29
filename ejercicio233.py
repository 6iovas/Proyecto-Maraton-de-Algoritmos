// Proyecto de Informatica
// Ejercicio 233
Ejercicio 26  (continuación) IDA* para el 8-puzzle (3×3) con heurística Manhattan
(Completo)
Diseño (recordatorio)
? IDA* iterativo: límite bound inicia en h(start) y aumenta al siguiente mínimo f observado cuando se corta.

? DFS recursivo con poda por f = g + h > bound y evitar retrocesos inmediatos.

? Cuando h == 0 hemos alcanzado la meta.

? Guardamos la secuencia de movimientos (opcional: valores movidos o posiciones).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int dx[4] = {-1,1,0,0}, dy[4] = {0,0,-1,1};
int manhattan(const array<int,9>& s){
    int res=0;
    for(int i=0;i<9;++i){
        int v = s[i];
        if(v==0) continue;
        int gx = (v-1)/3, gy = (v-1)%3;
        int x = i/3, y = i%3;
        res += abs(x - gx) + abs(y - gy);
    }
    return res;
}

bool dfsIDA(array<int,9>& state, int blank, int g, int bound, int prev_dir, vector<int>& moves, int& next_bound){
    int h = manhattan(state);
    int f = g + h;
    if(f > bound){
        next_bound = min(next_bound, f);
        return false;
    }
    if(h == 0) return true;
    int x = blank/3, y = blank%3;
    for(int dir=0; dir<4; ++dir){
        // avoid backtracking: if prev_dir is opposite of dir, skip
        if(prev_dir != -1 && (prev_dir ^ 1) == dir) continue;
        int nx = x + dx[dir], ny = y + dy[dir];
        if(nx<0 || ny<0 || nx>=3 || ny>=3) continue;
        int npos = nx*3 + ny;
        swap(state[blank], state[npos]);
        moves.push_back(state[blank]); // value moved into blank (optional record)
        if(dfsIDA(state, npos, g+1, bound, dir, moves, next_bound)) return true;
        moves.pop_back();
        swap(state[blank], state[npos]);
    }
    return false;
}

bool ida_star(array<int,9> start, vector<int>& out_moves){
    int start_blank = 0;
    for(int i=0;i<9;++i) if(start[i]==0){ start_blank = i; break; }
    int bound = manhattan(start);
    if(bound==0) return true;
    while(true){
        int next_bound = INT_MAX;
        vector<int> moves;
        array<int,9> st = start;
        if(dfsIDA(st, start_blank, 0, bound, -1, moves, next_bound)){
            out_moves = moves;
            return true;
        }
        if(next_bound==INT_MAX) return false; // no solution
        bound = next_bound;
        // Safety: set a reasonable limit to avoid infinite loops in pathological inputs
        if(bound > 50) return false; // 8-puzzle optimal solutions are usually <= 31
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // Input: 9 numbers row-major (0 is blank)
    array<int,9> start;
    for(int i=0;i<9;++i) if(!(cin>>start[i])) return 0;
    vector<int> moves;
    bool solved = ida_star(start, moves);
    if(!solved) { cout << "No solution found (or exceeds limit)\n"; return 0; }
    cout << "Solved in " << moves.size() << " moves\n";
    // print sequence of moved tiles (they are the tile values that moved into the blank)
    for(size_t i=0;i<moves.size();++i){
        cout << moves[i] << (i+1==moves.size()? '\n' : ' ');
    }
    return 0;
}

Pruebas
? Caso resuelto simple: 1 2 3 4 5 6 7 8 0 ? ya resuelto ? Solved in 0 moves.

? Caso sencillo: start 1 2 3 4 5 6 0 7 8 (requires 2 moves) ? expect Solved in 2 moves and sequence like 7 8 (values moved).

? Nota: IDA* en 8-puzzle es correcto con Manhattan heurística y encontrará solución óptima; límite de seguridad bound>50 evita loops en entradas insatisfactorias.