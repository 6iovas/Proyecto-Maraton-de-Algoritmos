// Proyecto de Informatica
// Ejercicio 49
Ejercicio 47: Longest Common Subsequence (LCS) (DP)
Análisis
 Encontrar longitud LCS entre dos strings.
Diseño
 DP 2D dp[i+1][j+1].
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string a,b; if(!(cin>>a>>b)) return 0;
    int n=a.size(), m=b.size();
    vector<vector<int>> dp(n+1, vector<int>(m+1,0));
    for(int i=1;i<=n;++i) for(int j=1;j<=m;++j){
        if(a[i-1]==b[j-1]) dp[i][j]=dp[i-1][j-1]+1;
        else dp[i][j]=max(dp[i-1][j], dp[i][j-1]);
    }
    cout<<dp[n][m]<<"\n";
    return 0;
}

Pruebas
? a="ABCBDAB", b="BDCAB" ? LCS length 3 (e.g., "BCB" or "BDAB"?).