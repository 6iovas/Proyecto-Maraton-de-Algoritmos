// Proyecto de Informatica
// Ejercicio 50
Ejercicio 48: Edit Distance (Levenshtein)
Análisis
 Mínimas operaciones (ins, del, rep) para convertir a en b.
Diseño
 DP 2D clásico.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string a,b; if(!(cin>>a>>b)) return 0;
    int n=a.size(), m=b.size();
    vector<vector<int>> dp(n+1, vector<int>(m+1,0));
    for(int i=0;i<=n;++i) dp[i][0]=i;
    for(int j=0;j<=m;++j) dp[0][j]=j;
    for(int i=1;i<=n;++i) for(int j=1;j<=m;++j){
        if(a[i-1]==b[j-1]) dp[i][j]=dp[i-1][j-1];
        else dp[i][j]=1+min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
    }
    cout<<dp[n][m]<<"\n";
    return 0;
}

Pruebas
? kitten ? sitting ? 3.