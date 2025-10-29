// Proyecto de Informatica
// Ejercicio 54
Ejercicio 52: Rod Cutting (DP)
Análisis
 Maximizar ingreso cortando varilla.
Diseño
 DP dp[i] max revenue length i.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> price(n+1);
    for(int i=1;i<=n;++i) cin>>price[i];
    vector<int> dp(n+1,0);
    for(int len=1; len<=n; ++len){
        for(int cut=1; cut<=len; ++cut) dp[len] = max(dp[len], price[cut] + dp[len-cut]);
    }
    cout<<dp[n]<<"\n";
    return 0;
}

Pruebas
? n=8 prices 1 5 8 9 10 17 17 20 ? best 22.