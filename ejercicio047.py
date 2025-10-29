// Proyecto de Informatica
// Ejercicio 47
Ejercicio 45: Contar número de subconjuntos con suma dada
Análisis
 Contar cuántas formas (mod no dado  aquí usar 64-bit).
Diseño
 DP 1D contable dp[s] += dp[s - a[i]].
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, S; if(!(cin>>n>>S)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    vector<ull> dp(S+1,0);
    dp[0]=1;
    for(int x: a){
        for(int s=S; s>=x; --s) dp[s] += dp[s-x];
    }
    cout << dp[S] << "\n";
    return 0;
}

Pruebas
? a=[1,1,1], S=2 ? 3.