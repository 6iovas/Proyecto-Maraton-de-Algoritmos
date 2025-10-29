// Proyecto de Informatica
// Ejercicio 188
Ejercicio 184: Partition equal subset sum
Análisis
 ¿Se puede particionar en dos subconjuntos con misma suma?
Diseño
 Subset sum target = total/2 boolean DP.
Código
#include <bits/stdc++.h>
using namespace std;
int main(){ int n; if(!(cin>>n)) return 0; vector<int>a(n); int sum=0; for(int i=0;i<n;++i){cin>>a[i]; sum+=a[i];}
 if(sum%2){ cout<<"NO\n"; return 0; }
 int S=sum/2; vector<char> dp(S+1,0); dp[0]=1;
 for(int x:a) for(int s=S;s>=x;--s) if(dp[s-x]) dp[s]=1;
 cout<<(dp[S]?"YES\n":"NO\n");
}

Prueba
? 4 1 5 11 5 ? YES