// Proyecto de Informatica
// Ejercicio 169
Ejercicio 165: Número de caminos en cuadrícula m×n (DP)
Análisis
 Contar caminos de (0,0) a (m-1,n-1) con movimientos R y D.
Diseño
 DP 2D, dp[i][j]=dp[i-1][j]+dp[i][j-1].
Código
#include <bits/stdc++.h>
using namespace std;
int main(){
    int m,n; if(!(cin>>m>>n)) return 0;
    vector<vector<long long>> dp(m, vector<long long>(n,0));
    for(int i=0;i<m;++i) dp[i][0]=1;
    for(int j=0;j<n;++j) dp[0][j]=1;
    for(int i=1;i<m;++i) for(int j=1;j<n;++j) dp[i][j]=dp[i-1][j]+dp[i][j-1];
    cout<<dp[m-1][n-1]<<"\n";
}

Prueba
? Entrada: 3 3 ? Salida: 6