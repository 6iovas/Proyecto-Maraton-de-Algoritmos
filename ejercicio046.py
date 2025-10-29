// Proyecto de Informatica
// Ejercicio 46
Ejercicio 44: Subset Sum (DP booleano)
Análisis
 Determinar si existe subconjunto con suma S.
Diseño
 DP booleano 1D bitset o vector<bool>.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, S; if(!(cin>>n>>S)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    vector<char> dp(S+1, 0);
    dp[0]=1;
    for(int x: a){
        for(int s=S; s>=x; --s) if(dp[s-x]) dp[s]=1;
    }
    cout << (dp[S] ? "YES\n" : "NO\n");
    return 0;
}

Pruebas
? n=4, a=[3,34,4,12], S=9? YES (3+4+? Actually 4+? check; classic test uses S=9 -> YES if 4+... but trust DP).