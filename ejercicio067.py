// Proyecto de Informatica
// Ejercicio 67
Ejercicio 65: Edmonds-Karp  Maximum Flow (BFS augmenting path)
Análisis
 Implementación de Edmonds-Karp (Ford-Fulkerson con BFS), capacidad entera.
Diseño
 Residual graph + BFS para hallar path con capacidad.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Edge{int to; int rev; ll cap;};
struct MaxFlow {
    int n; vector<vector<Edge>> g;
    MaxFlow(int n):n(n),g(n){}
    void addEdge(int u,int v,ll c){ g[u].push_back({v,(int)g[v].size(),c}); g[v].push_back({u,(int)g[u].size()-1,0}); }
    ll maxflow(int s,int t){
        ll flow=0;
        while(true){
            vector<int> parent(n, -1), pe(n, -1);
            queue<int> q; q.push(s); parent[s]=s;
            while(!q.empty() && parent[t]==-1){
                int u=q.front();q.pop();
                for(int i=0;i<(int)g[u].size();++i){
                    auto &e=g[u][i];
                    if(parent[e.to]==-1 && e.cap>0){ parent[e.to]=u; pe[e.to]=i; q.push(e.to); }
                }
            }
            if(parent[t]==-1) break;
            ll add = LLONG_MAX;
            for(int v=t; v!=s; v=parent[v]){ auto &e = g[parent[v]][pe[v]]; add = min(add, e.cap); }
            for(int v=t; v!=s; v=parent[v]){ auto &e = g[parent[v]][pe[v]]; e.cap -= add; g[v][e.rev].cap += add; }
            flow += add;
        }
        return flow;
    }
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    MaxFlow mf(n);
    for(int i=0;i<m;++i){ int u,v; long long c; cin>>u>>v>>c; mf.addEdge(u,v,c); }
    int s,t; cin>>s>>t;
    cout<<mf.maxflow(s,t)<<"\n";
    return 0;
}

Pruebas
? Pequeño network flow example.