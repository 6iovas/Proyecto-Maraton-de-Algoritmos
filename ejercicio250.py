// Proyecto de Informatica
// Ejercicio 250
? Compute maximum matching (HopcroftKarp) as in Ejercicio 16.

? Build directed alternating graph or simply run DFS from all unmatched left nodes along edges not in matching then along matching edges alternately to mark reachable vertices.

? Derive vertex cover nodes as stated.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
// We'll reuse HopcroftKarp from earlier (slightly adjusted to expose match arrays)
struct HopcroftKarp {
    int nL, nR;
    vector<vector<int>> adj;
    vector<int> pairU, pairV, dist;
    const int INF = 1e9;
    HopcroftKarp(int nL, int nR): nL(nL), nR(nR), adj(nL), pairU(nL,-1), pairV(nR,-1), dist(nL) {}
    void addEdge(int u,int v){ adj[u].push_back(v); }
    bool bfs(){
        queue<int> q;
        for(int u=0;u<nL;++u){
            if(pairU[u]==-1){ dist[u]=0; q.push(u); }
            else dist[u]=INF;
        }
        bool reachable=false;
        while(!q.empty()){
            int u=q.front(); q.pop();
            for(int v: adj[u]){
                if(pairV[v]!=-1 && dist[pairV[v]]==INF){
                    dist[pairV[v]] = dist[u]+1;
                    q.push(pairV[v]);
                }
                if(pairV[v]==-1) reachable=true;
            }
        }
        return reachable;
    }
    bool dfs(int u){
        for(int v: adj[u]){
            if(pairV[v]==-1 || (dist[pairV[v]]==dist[u]+1 && dfs(pairV[v]))){
                pairU[u]=v; pairV[v]=u; return true;
            }
        }
        dist[u]=INF; return false;
    }
    int maxMatching(){
        int matching=0;
        while(bfs()){
            for(int u=0;u<nL;++u)
                if(pairU[u]==-1 && dfs(u)) ++matching;
        }
        return matching;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int nL,nR,m; if(!(cin>>nL>>nR>>m)) return 0;
    HopcroftKarp hk(nL,nR);
    for(int i=0;i<m;++i){ int u,v; cin>>u>>v; hk.addEdge(u,v); }
    int mm = hk.maxMatching();
    cout<<"Maximum matching size: "<<mm<<"\n";
    // find min vertex cover from matching
    vector<char> visL(nL, false), visR(nR, false);
    queue<int> q;
    for(int u=0; u<nL; ++u) if(hk.pairU[u]==-1){ q.push(u); visL[u]=true; }
    while(!q.empty()){
        int u = q.front(); q.pop();
        for(int v: hk.adj[u]){
            if(!visR[v] && hk.pairU[u] != v){ // traverse non-matching edge u->v
                visR[v]=true;
                if(hk.pairV[v]!=-1 && !visL[hk.pairV[v]]){
                    visL[hk.pairV[v]] = true;
                    q.push(hk.pairV[v]);
                }
            }
        }
    }
    // min vertex cover = (L \ reachable) U (R ? reachable)
    vector<int> coverL, coverR;
    for(int u=0; u<nL; ++u) if(!visL[u]) coverL.push_back(u);
    for(int v=0; v<nR; ++v) if(visR[v]) coverR.push_back(v);
    cout<<"Minimum Vertex Cover size: "<<(coverL.size()+coverR.size())<<"\n";
    cout<<"Left vertices in cover:";
    for(int x: coverL) cout<<" "<<x;
    cout<<"\nRight vertices in cover:";
    for(int x: coverR) cout<<" "<<x;
    cout<<"\n";
    return 0;
}

Pruebas
? Example bipartite graph:

? Left 3 (0,1,2), Right 3 (0,1,2)

? Edges: 0-0, 0-1, 1-1, 2-2

? Maximum matching size = 3 ? Minimum vertex cover size = 3. The algorithm will output a valid cover (e.g., Left {} and Right {0,1,2} or combinations depending on matching).