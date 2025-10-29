// Proyecto de Informatica
// Ejercicio 211
Ejercicio 6  Dinic (Max Flow) implementación eficiente (adj list + level graph + ptr array)
Análisis del problema
 Implementar Dinic para hallar flujo máximo en grafo dirigido con n nodos y m aristas con capacidades no negativas (integers). Debe ser eficiente para grafos medianos/grandes (m hasta ~1e5).
Diseño de la solución
? Grafo con aristas con to, rev_index, cap.

? bfs para construir level graph.

? dfs con ptr para escanear aristas sin repetir.

? Complejidad promedio buena: O(m * sqrt(n)) en práctica o O(min(n^2/3, m^1/2)*m) teórico.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct Edge { int to; int rev; long long cap; };
struct Dinic {
    int n; vector<vector<Edge>> g; vector<int> level, ptr;
    Dinic(int n): n(n), g(n), level(n), ptr(n) {}
    void addEdge(int u, int v, long long c){
        Edge a = {v, (int)g[v].size(), c};
        Edge b = {u, (int)g[u].size(), 0};
        g[u].push_back(a); g[v].push_back(b);
    }
    bool bfs(int s, int t){
        fill(level.begin(), level.end(), -1);
        queue<int> q; q.push(s); level[s]=0;
        while(!q.empty()){
            int v=q.front(); q.pop();
            for(const Edge &e: g[v]) if(e.cap>0 && level[e.to]==-1){
                level[e.to]=level[v]+1; q.push(e.to);
            }
        }
        return level[t]!=-1;
    }
    long long dfs(int v, int t, long long pushed){
        if(pushed==0) return 0;
        if(v==t) return pushed;
        for(int &cid = ptr[v]; cid < (int)g[v].size(); ++cid){
            Edge &e = g[v][cid];
            if(e.cap>0 && level[e.to]==level[v]+1){
                long long tr = dfs(e.to, t, min(pushed, e.cap));
                if(tr>0){
                    e.cap -= tr;
                    g[e.to][e.rev].cap += tr;
                    return tr;
                }
            }
        }
        return 0;
    }
    long long maxflow(int s, int t){
        long long flow = 0;
        while(bfs(s,t)){
            fill(ptr.begin(), ptr.end(), 0);
            while(long long pushed = dfs(s,t,LLONG_MAX)) flow += pushed;
        }
        return flow;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    Dinic D(n);
    for(int i=0;i<m;++i){
        int u,v; long long c; cin>>u>>v>>c;
        D.addEdge(u,v,c);
    }
    int s,t; cin>>s>>t;
    cout << "MaxFlow: " << D.maxflow(s,t) << '\n';
    return 0;
}

Pruebas
? Pequeño grafo con known maxflow (e.g., classic sample), comparar resultado.