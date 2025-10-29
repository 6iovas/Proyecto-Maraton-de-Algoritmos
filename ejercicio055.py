// Proyecto de Informatica
// Ejercicio 55
Ejercicio 53: Coin change  número de formas (DP)
Análisis
 Contar formas de hacer sum con monedas (order not important).
Diseño
 DP 1D acumulando por monedas.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int m, sum; if(!(cin>>m>>sum)) return 0;
    vector<int> coins(m);
    for(int i=0;i<m;++i) cin>>coins[i];
    vector<ull> dp(sum+1,0);
    dp[0]=1;
    for(int c: coins) for(int s=c; s<=sum; ++s) dp[s] += dp[s-c];
    cout<<dp[sum]<<"\n";
    return 0;
}

Pruebas
? coins [1,2,3], sum 4 ? ways 4.