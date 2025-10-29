// Proyecto de Informatica
// Ejercicio 52
Ejercicio 50: Maximum sum increasing subsequence
Análisis
 Encontrar subsecuencia estrictamente creciente con suma máxima.
Diseño
 DP dp[i] = max sum of inc subseq ending at i.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    for(int i=0;i<n;++i) cin>>a[i];
    vector<long long> dp(n);
    long long ans = LLONG_MIN;
    for(int i=0;i<n;++i){
        dp[i]=a[i];
        for(int j=0;j<i;++j) if(a[j]<a[i]) dp[i]=max(dp[i], dp[j]+a[i]);
        ans = max(ans, dp[i]);
    }
    cout<<ans<<"\n";
    return 0;
}

Pruebas
? a=[1,101,2,3,100,4,5] ? 106 (1+2+3+100)