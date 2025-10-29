// Proyecto de Informatica
// Ejercicio 274
Ejercicio 43  K-Shortest Paths (Yens algorithm using Dijkstra)
Análisis
 Encontrar las K primeras rutas distintas (simple paths) ordenadas por cost between s and t. Yens algorithm uses repeated shortest path computations with temporary edge/node removals. Works well for moderate graphs and small K.
Diseño
? Compute shortest path P0 (Dijkstra).

? For k=1..K-1, for each node i on P_{k-1} do: root = prefix up to node i; temporarily remove edges that would create paths already found with same root; compute spur path from node i to t; combine root+spur ? candidate; collect candidates in min-heap by total cost; pick cheapest new candidate as P_k.

? Complexity: O(K * n * (m log n)) in worst case.

Código (C++) (compact, works for weighted graph)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = (1LL<<60);

struct Edge { int to; ll w; int id; };
struct Graph {
    int n; vector<vector<Edge>> g;
    Graph(int n):n(n),g(n){}
    void addEdge(int u,int v,ll w,int id){ g[u].push_back({v,w,id}); }
    vector<ll> dijkstra(int s, vector<int>& parent_node, vector<int>& parent_edge, 
                        const vector<char>& removed_node, const vector<char>& removed_edge){
        parent_node.assign(n,-1); parent_edge.assign(n,-1);
        vector<ll> dist(n, INF);
        using pli = pair<ll,int>;
        priority_queue<pli, vector<pli>, greater<pli>> pq;
        dist[s]=0; pq.push({0,s});
        while(!pq.empty()){
            auto [d,u]=pq.top(); pq.pop();
            if(d!=dist[u]) continue;
            if(removed_node[u]) continue;
            for(auto &e: g[u]){
                if(removed_edge[e.id]) continue;
                int v=e.to;
                if(removed_node[v]) continue;
                if(dist[v] > d + e.w){
                    dist[v] = d + e.w;
                    parent_node[v] = u; parent_edge[v] = e.id;
                    pq.push({dist[v], v});
                }
            }
        }
        return dist;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    Graph G(n);
    for(int i=0;i<m;++i){ int u,v; long long w; cin>>u>>v>>w; G.addEdge(u,v,w,i); }
    int s,t,K; cin>>s>>t>>K;
    vector<vector<int>> A_paths; // store node sequences
    vector<ll> A_costs;
    // initial shortest path
    vector<int> parent_node, parent_edge;
    vector<char> removed_node(n,0), removed_edge(m,0);
    auto dist = G.dijkstra(s, parent_node, parent_edge, removed_node, removed_edge);
    if(dist[t]==INF){ cout<<"No path\n"; return 0; }
    // reconstruct path nodes
    auto get_path_nodes = [&](int dest){
        vector<int> path;
        for(int v=dest; v!=-1; v=parent_node[v]) path.push_back(v);
        reverse(path.begin(), path.end());
        return path;
    };
    A_paths.push_back(get_path_nodes(t));
    A_costs.push_back(dist[t]);
    // candidates (cost, path nodes)
    using Item = pair<ll, vector<int>>;
    priority_queue<Item, vector<Item>, greater<Item>> cand;
    for(int k=1;k<K;++k){
        for(int i=0;i+1<(int)A_paths[k-1].size(); ++i){
            int spurNode = A_paths[k-1][i];
            vector<int> rootPath(A_paths[k-1].begin(), A_paths[k-1].begin()+i+1);
            // remove edges that share the same rootPath in previous A_paths
            fill(removed_edge.begin(), removed_edge.end(), 0);
            fill(removed_node.begin(), removed_node.end(), 0);
            for(auto &p: A_paths){
                if(p.size() > i && equal(rootPath.begin(), rootPath.end(), p.begin())){
                    // remove edge p[i] -> p[i+1] by finding its id
                    int u = p[i], v = p[i+1];
                    for(auto &e: G.g[u]) if(e.to==v) removed_edge[e.id]=1;
                }
            }
            // remove nodes in rootPath except spurNode
            for(int r=0;r+1<=(int)rootPath.size()-1;++r) if(rootPath[r]!=spurNode) removed_node[rootPath[r]]=1;
            auto dist2 = G.dijkstra(spurNode, parent_node, parent_edge, removed_node, removed_edge);
            if(dist2[t]==INF) continue;
            // build spur path nodes
            vector<int> spurPath;
            for(int v=t; v!=-1; v=parent_node[v]) spurPath.push_back(v);
            reverse(spurPath.begin(), spurPath.end());
            vector<int> total = rootPath;
            total.pop_back();
            total.insert(total.end(), spurPath.begin(), spurPath.end());
            ll totalCost = 0;
            // compute cost by summing edges along `total`
            for(int idx=0; idx+1<total.size(); ++idx){
                int u=total[idx], v=total[idx+1];
                // find edge weight (first occurrence)
                for(auto &e: G.g[u]) if(e.to==v){ totalCost += e.w; break; }
            }
            cand.push({totalCost, total});
        }
        if(cand.empty()) break;
        auto best = cand.top(); cand.pop();
        A_costs.push_back(best.first);
        A_paths.push_back(best.second);
    }
    for(size_t i=0;i<A_paths.size();++i){
        cout<<"Path "<<i<<": cost="<<A_costs[i]<<" nodes:";
        for(int v:A_paths[i]) cout<<" "<<v;
        cout<<"\n";
    }
    return 0;
}

Pruebas
? Small directed graph where multiple distinct k-shortest paths exist; check listed paths ordered by cost.