// Proyecto de Informatica
// Ejercicio 187
Ejercicio 183: Subset sum count (DP counting)
Análisis
 Contar formas para sumar S.
Diseño
 DP 1D counts (unsigned long long).
Código
#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
int main(){ int n,S; if(!(cin>>n>>S)) return 0; vector<int>a(n); for(int i=0;i<n;++i)cin>>a[i];
 vector<ull> dp(S+1); dp[0]=1;
 for(int x:a) for(int s=S;s>=x;--s) dp[s]+=dp[s-x];
 cout<<dp[S]<<"\n"; }

Prueba
? a=[1,1,1], S=2 ? 3