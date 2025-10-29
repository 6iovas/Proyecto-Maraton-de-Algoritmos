// Proyecto de Informatica
// Ejercicio 53
Ejercicio 51: Matrix Chain Multiplication (DP)
Análisis
 Minimizar coste de multiplicación de matrices.
Diseño
 DP 2D dp[i][j] min coste.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0; // number of matrices = n-1 if dims size n
    vector<int> dims(n);
    for(int i=0;i<n;++i) cin>>dims[i];
    vector<vector<long long>> dp(n, vector<long long>(n,0));
    for(int len=2; len<n; ++len){
        for(int i=0;i+len<n;++i){
            int j=i+len;
            dp[i][j]=LLONG_MAX;
            for(int k=i+1;k<j;++k){
                dp[i][j]=min(dp[i][j], dp[i][k]+dp[k][j]+ (long long)dims[i]*dims[k]*dims[j]);
            }
        }
    }
    cout<<dp[0][n-1]<<"\n";
    return 0;
}

Pruebas
? dims [40 20 30 10 30] ? min cost 26000.