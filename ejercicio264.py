// Proyecto de Informatica
// Ejercicio 264
Ejercicio 36  Minimum Mean Cycle (Karps algorithm)
Analysis
 Find directed cycle with minimum average weight (mean weight per edge) in O(n*m) using Karp.
Design
 Compute dp[k][v] = min weight of path length k ending at v. Then for each v compute max over k of (dp[n][v] - dp[k][v])/(n-k) and take minimum over v.
Code (C++)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 4e18;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m; if(!(cin>>n>>m)) return 0;
    vector<vector<pair<int,ll>>> g(n);
    for(int i=0;i<m;++i){ int u,v; ll w; cin>>u>>v>>w; g[u].push_back({v,w}); }
    vector<vector<ll>> dp(n+1, vector<ll>(n, INF));
    // dp[0][v] = 0 for all v
    for(int v=0; v<n; ++v) dp[0][v]=0;
    for(int k=1;k<=n;++k){
        for(int v=0; v<n; ++v){
            for(auto &e: g[v]){ int to = e.first; ll w = e.second; if(dp[k-1][v]<INF) dp[k][to] = min(dp[k][to], dp[k-1][v] + w); }
        }
    }
    double ans = 1e300;
    for(int v=0; v<n; ++v){
        if(dp[n][v] >= INF) continue;
        double maxAvg = -