// Proyecto de Informatica
// Ejercicio 272
? Igual que ejercicio 21 pero detener cuando flow == F o no hay camino.

? Guardar for each augment the path and amount augmented if user wants reconstruct route(s).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
struct Edge{ int to, rev; int cap; long long cost; };
struct MCMF {
    int n; vector<vector<Edge>> g;
    MCMF(int n): n(n), g(n) {}
    void addEdge(int u,int v,int cap,long long cost){
        g[u].push_back({v, (int)g[v].size(), cap, cost});
        g[v].push_back({u, (int)g[u].size()-1, 0, -cost});
    }
    // returns {flow, cost}
    pair<int,long long> minCostFlowWithLimit(int s,int t,int F){
        int flow=0; long long cost=0;
        vector<long long> pot(n,0), dist(n);
        vector<int> pv(n), pe(n);
        const long long INFLL = (1LL<<60);
        while(flow < F){
            // Dijkstra
            fill(dist.begin(), dist.end(), INFLL);
            dist[s]=0;
            priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
            pq.push({0,s});
            while(!pq.empty()){
                auto [d,u] = pq.top(); pq.pop();
                if(d != dist[u]) continue;
                for(int i=0;i<(int)g[u].size();++i){
                    Edge &e = g[u][i];
                    if(e.cap<=0) continue;
                    long long nd = d + e.cost + pot[u] - pot[e.to];
                    if(nd < dist[e.to]){
                        dist[e.to] = nd; pv[e.to]=u; pe[e.to]=i; pq.push({nd,e.to});
                    }
                }
            }
            if(dist[t]==INFLL) break;
            for(int i=0;i<n;++i) if(dist[i]<INFLL) pot[i]+=dist[i];
            int add = F - flow;
            for(int v=t; v!=s; v=pv[v]) add = min(add, g[pv[v]][pe[v]].cap);
            for(int v=t; v!=s; v=pv[v]){
                Edge &e = g[pv[v]][pe[v]];
                e.cap -= add;
                g[v][e.rev].cap += add;
            }
            flow += add;
            cost += 1LL * add * pot[t];
        }
        return {flow, cost};
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    MCMF M(n);
    for(int i=0;i<m;++i){ int u,v,cap; long long cost; cin>>u>>v>>cap>>cost; M.addEdge(u,v,cap,cost); }
    int s,t,F; cin>>s>>t>>F;
    auto res = M.minCostFlowWithLimit(s,t,F);
    if(res.first < F) cout<<"Impossible to send required flow\n";
    else cout<<"Flow="<<res.first<<" Cost="<<res.second<<"\n";
    return 0;
}

Pruebas
? Small graph with limited capacities; request F larger than maxflow ? "Impossible".