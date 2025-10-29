// Proyecto de Informatica
// Ejercicio 282
Ejercicio 49  Maximum Flow with capacity scaling (Dinic variant improvement)
Análisis
 Implement capacity scaling improvement for Dinic/Edmonds-Karp: process capacities in decreasing powers of two to speed up in graphs with large capacities. Simpler approach: use Dinic (exercise 6) but this exercise shows capacity scaling conceptually.
Diseño
? Repeatedly run blocking flow considering only edges with cap >= scale, reduce scale by half.

Código (C++)
// For brevity reuse Dinic structure and apply capacity thresholding by temporarily ignoring small edges in BFS/DFS
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
struct Edge{ int to, rev; ll cap; };
struct DinicScaling {
    int n; vector<vector<Edge>> g;
    DinicScaling(int n):n(n),g(n){}
    void addEdge(int u,int v,ll c){
        g[u].push_back({v,(int)g[v].size(),c});
        g[v].push_back({u,(int)g[u].size()-1,0});
    }
    vector<int> level, ptr;
    bool bfs(int s,int t, ll threshold){
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[s]=0; q.push(s);
        while(!q.empty()){
            int v=q.front(); q.pop();
            for(auto &e: g[v]){
                if(level[e.to]==-1 && e.cap >= threshold){
                    level[e.to]=level[v]+1; q.push(e.to);
                }
            }
        }
        return level[t]!=-1;
    }
    ll dfs(int v,int t,ll pushed, ll threshold){
        if(!pushed) return 0;
        if(v==t) return pushed;
        for(int &cid = ptr[v]; cid<(int)g[v].size(); ++cid){
            Edge &e = g[v][cid];
            if(level[e.to] != level[v]+1 || e.cap < threshold) continue;
            ll tr = dfs(e.to, t, min(pushed, e.cap), threshold);
            if(tr){
                e.cap -= tr; g[e.to][e.rev].cap += tr; return tr;
            }
        }
        return 0;
    }
    ll maxflow(int s,int t){
        ll flow=0;
        ll maxCap=0;
        for(int i=0;i<n;++i) for(auto &e: g[i]) maxCap = max(maxCap, e.cap);
        level.assign(n, -1); ptr.assign(n,0);
        for(ll scale = 1LL<< (63 - __builtin_clzll(maxCap)); scale>0; scale >>=1){
            while(bfs(s,t,scale)){
                fill(ptr.begin(), ptr.end(), 0);
                while(ll pushed = dfs(s,t,LLONG_MAX, scale)) flow += pushed;
            }
        }
        return flow;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    DinicScaling D(n);
    for(int i=0;i<m;++i){ int u,v; long long c; cin>>u>>v>>c; D.addEdge(u,v,c); }
    int s,t; cin>>s>>t;
    cout<<D.maxflow(s,t)<<"\n";
    return 0;
}

Pruebas
? Compare with Dinic for same graph; results equal.