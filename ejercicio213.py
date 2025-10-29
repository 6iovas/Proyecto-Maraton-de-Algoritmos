// Proyecto de Informatica
// Ejercicio 213
Ejercicio 8  Longest Common Subsequence con reconstrucción (DP O(nm))
Análisis del problema
 Dadas dos strings A y B (longitudes n,m ? ~2000), hallar la longitud de la LCS y reconstruir una LCS. Uso de DP O(n*m).
Diseño de la solución
? DP dp[i][j] = LCS length of A[0..i-1] and B[0..j-1].

? Transición: if A[i-1]==B[j-1] dp[i][j]=dp[i-1][j-1]+1 else max(dp[i-1][j], dp[i][j-1]).

? Reconstrucción retrocediendo desde dp[n][m].

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string A,B; if(!(cin>>A>>B)) return 0;
    int n=A.size(), m=B.size();
    vector<vector<int>> dp(n+1, vector<int>(m+1,0));
    for(int i=1;i<=n;++i) for(int j=1;j<=m;++j){
        if(A[i-1]==B[j-1]) dp[i][j]=dp[i-1][j-1]+1;
        else dp[i][j]=max(dp[i-1][j], dp[i][j-1]);
    }
    cout<<"LCS length: "<<dp[n][m]<<"\n";
    // reconstruct one LCS
    string lcs;
    int i=n,j=m;
    while(i>0 && j>0){
        if(A[i-1]==B[j-1]){ lcs.push_back(A[i-1]); --i; --j; }
        else if(dp[i-1][j] >= dp[i][j-1]) --i;
        else --j;
    }
    reverse(lcs.begin(), lcs.end());
    cout<<"LCS: "<<lcs<<"\n";
    return 0;
}

Pruebas
? A="ABCBDAB" B="BDCABA" ? LCS length 4 (one LCS: BCBA or BDAB depending on path); code returns a valid LCS.