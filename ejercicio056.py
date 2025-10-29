// Proyecto de Informatica
// Ejercicio 56
Ejercicio 54: Coin change  mínimo número de monedas
Análisis
 Min coins to make sum (unbounded).
Diseño
 DP dp[s] = min(dp[s], dp[s-c]+1).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m,sum; if(!(cin>>m>>sum)) return 0;
    vector<int> coins(m);
    for(int i=0;i<m;++i) cin>>coins[i];
    vector<int> dp(sum+1, INF);
    dp[0]=0;
    for(int c: coins) for(int s=c; s<=sum; ++s) dp[s] = min(dp[s], dp[s-c]+1);
    cout << (dp[sum]==INF ? -1 : dp[sum]) << "\n";
    return 0;
}

Pruebas
? coins [1,3,4], sum 6 ? 2 (3+3 or 4+1+1? min 2).