// Proyecto de Informatica
// Ejercicio 189
Ejercicio 185: TSP (bitmask DP)  costo minimal (n ? 16)
Análisis
 DP sobre subsets: dp[mask][i] min cost to reach mask ending at i.
Diseño
 Standard bitmask DP O(n^2 2^n).
Código (esqueleto)
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll INF = 1e15;
int main(){
    int n; if(!(cin>>n)) return 0;
    vector<vector<ll>> w(n, vector<ll>(n));
    for(int i=0;i<n;++i) for(int j=0;j<n;++j) cin>>w[i][j];
    int N = 1<<n;
    vector<vector<ll>> dp(N, vector<ll>(n, INF));
    dp[1][0]=0; // start at 0
    for(int mask=1; mask<N; ++mask)
        for(int u=0; u<n; ++u) if(dp[mask][u]<INF)
            for(int v=0; v<n; ++v) if(!(mask & (1<<v)))
                dp[mask | (1<<v)][v] = min(dp[mask | (1<<v)][v], dp[mask][u] + w[u][v]);
    ll ans = INF;
    for(int u=0; u<n; ++u) ans = min(ans, dp[N-1][u] + w[u][0]);
    cout<<ans<<"\n";
}

Prueba
? n small (4) with symmetric weights; check reachable.