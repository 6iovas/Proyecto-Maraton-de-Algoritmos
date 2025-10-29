// Proyecto de Informatica
// Ejercicio 231
Ejercicio 25  2-SAT (implication graph + SCC)
Análisis
 Resolver fórmulas booleanas en forma CNF con cláusulas 2-literales (2-SAT). Construir grafo de implicación (a->b) y usar SCC (Tarjan) para decidir satisfacibilidad: una variable y su negación no deben pertenecer a la misma SCC. Además reconstruir asignación topológica sobre componentes.
Diseño
? Mapear variable x a índices 2*i (x false?) convención: use id(x)=2*i for false? Commonly: for var i: node 2i = i (value false?), 2i^1 toggles. We'll use: node 2*i -> false, 2*i+1 -> true. For literal x (positive), use 2*i+1; for !x use 2*i. Clause (a or b) => (!a -> b) and (!b -> a).

? Build graph, run SCC, check conflicts, build assignment by component order (higher comp id earlier = earlier in topological order).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
// 2-SAT: vars indexed 0..n-1
struct TwoSAT {
    int n;
    vector<vector<int>> g;
    TwoSAT(int n): n(n), g(2*n) {}
    inline int var(int x, bool val){ return 2*x + (val?1:0); }
    inline int neg(int v){ return v^1; }
    // add implication u -> v
    void addImp(int u, int v){ g[u].push_back(v); }
    // add clause (x_val ? x : !x) OR (y_val ? y : !y)
    void addOr(int x,int xval,int y,int yval){
        int a = var(x, xval), b = var(y, yval);
        addImp(neg(a), b);
        addImp(neg(b), a);
    }
    // SCC (Kosaraju)
    vector<int> order, comp, used;
    void dfs1(int v){
        used[v]=1;
        for(int to:g[v]) if(!used[to]) dfs1(to);
        order.push_back(v);
    }
    void dfs2(int v,int cl, vector<vector<int>>& rg){
        comp[v]=cl;
        for(int to: rg[v]) if(comp[to]==-1) dfs2(to,cl,rg);
    }
    bool solve(vector<int>& assignment){
        int N = 2*n;
        used.assign(N,0); order.clear();
        for(int i=0;i<N;++i) if(!used[i]) dfs1(i);
        vector<vector<int>> rg(N);
        for(int v=0; v<N; ++v) for(int to: g[v]) rg[to].push_back(v);
        comp.assign(N,-1);
        int j=0;
        for(int i=N-1;i>=0;--i) if(comp[order[i]]==-1) dfs2(order[i], j++, rg);
        assignment.assign(n,0);
        for(int i=0;i<n;++i){
            if(comp[2*i]==comp[2*i+1]) return false;
            assignment[i] = comp[2*i] < comp[2*i+1]; // comp larger means earlier? depends on implementation; this gives a valid assignment
        }
        return true;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    TwoSAT solver(n);
    // input each clause: a sign (+/-) var, b sign var, format like "1 -2" means x1 OR !x2?
    // For simplicity read clauses as four ints: x, sgnx, y, sgny where sgn=1 means positive, 0 negative
    for(int i=0;i<m;++i){
        int x, sx, y, sy; cin>>x>>sx>>y>>sy;
        // convert 1-based var to 0-based
        solver.addOr(x-1, sx, y-1, sy);
    }
    vector<int> assign;
    if(solver.solve(assign)){
        cout<<"SAT\n";
        for(int i=0;i<n;++i) cout<<assign[i]<<" ";
        cout<<"\n";
    } else cout<<"UNSAT\n";
    return 0;
}

Pruebas
? Clause example for (x1 OR x2) and (!x1 OR !x2) etc. Input format: see comments.