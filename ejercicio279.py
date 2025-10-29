// Proyecto de Informatica
// Ejercicio 279
Ejercicio 46  Re-rooting DP on Tree (compute answer for every root)  example: sum of distances from root to all nodes
Análisis
 Compute for every node v the sum of distances from v to all other nodes. Use two DFS passes: first compute subtree sizes and dp[root]=sum distances from root; second pass reroot transferring values.
Diseño
? dfs1(u,p) computes sz[u] and dp[u] = sum distances from u to nodes in its subtree.

? dfs2(u,p) uses parent result to compute answer for children: ans[v] = ans[u] - sz[v] + (n - sz[v]).

Código (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int n;
vector<vector<int>> g;
vector<int> sz;
vector<ll> dp, ans;

void dfs1(int u,int p){
    sz[u]=1; dp[u]=0;
    for(int v: g[u]) if(v!=p){
        dfs1(v,u);
        sz[u]+=sz[v];
        dp[u] += dp[v] + sz[v];
    }
}
void dfs2(int u,int p){
    ans[u] = dp[u];
    for(int v: g[u]) if(v!=p){
        ll du = dp[u], dv = dp[v];
        int su = sz[u], sv = sz[v];
        // reroot u->v
        dp[u] -= (dp[v] + sz[v]);
        sz[u] -= sz[v];
        dp[v] += (dp[u] + sz[u]);
        sz[v] += sz[u];
        dfs2(v,u);
        // restore
        dp[u]=du; dp[v]=dv; sz[u]=su; sz[v]=sv;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if(!(cin>>n)) return 0;
    g.assign(n, {});
    for(int i=0;i<n-1;++i){ int u,v; cin>>u>>v; g[u].push_back(v); g[v].push_back(u); }
    sz.assign(n,0); dp.assign(n,0); ans.assign(n,0);
    dfs1(0,-1);
    dfs2(0,-1);
    for(int i=0;i<n;++i) cout<<ans[i]<<(i+1==n?'\n':' ');
    return 0;
}

Pruebas
? Tree line of 4 nodes 0-1-2-3. Sum distances: node0->6, node1->4, node2->4, node3->6.