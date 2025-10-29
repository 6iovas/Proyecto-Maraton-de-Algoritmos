// Proyecto de Informatica
// Ejercicio 51
Ejercicio 49: Partition problem (dividir en dos subconjuntos iguales)
Análisis
 Determinar si suma total es par y existe subset con suma total/2.
Diseño
 Usar Subset Sum (DP booleano).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    vector<int> a(n);
    long long sum=0;
    for(int i=0;i<n;++i){ cin>>a[i]; sum+=a[i]; }
    if(sum%2){ cout<<"NO\n"; return 0; }
    int S=sum/2;
    vector<char> dp(S+1,0); dp[0]=1;
    for(int x: a) for(int s=S; s>=x; --s) if(dp[s-x]) dp[s]=1;
    cout << (dp[S] ? "YES\n" : "NO\n");
    return 0;
}

Pruebas
? a=[1,5,11,5] ? YES (11 = 11? actually partition 11|11).

? a=[1,2,3,5] ? NO.