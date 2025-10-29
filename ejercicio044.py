// Proyecto de Informatica
// Ejercicio 44
Ejercicio 42: Knapsack 0/1 con reconstrucción del conjunto óptimo
Análisis
 Además de valor máximo, obtener indices seleccionados.
Diseño
 DP 2D para reconstrucción.
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,W; if(!(cin>>n>>W)) return 0;
    vector<int> w(n), v(n);
    for(int i=0;i<n;++i) cin>>w[i]>>v[i];
    vector<vector<int>> dp(n+1, vector<int>(W+1,0));
    for(int i=1;i<=n;++i)
        for(int cap=0; cap<=W; ++cap){
            dp[i][cap] = dp[i-1][cap];
            if (cap >= w[i-1]) dp[i][cap] = max(dp[i][cap], dp[i-1][cap-w[i-1]] + v[i-1]);
        }
    cout << dp[n][W] << "\n";
    int cap = W;
    vector<int> chosen;
    for(int i=n;i>=1;--i){
        if (dp[i][cap] != dp[i-1][cap]){
            chosen.push_back(i-1);
            cap -= w[i-1];
        }
    }
    reverse(chosen.begin(), chosen.end());
    for(int idx: chosen) cout << idx << " ";
    cout << "\n";
    return 0;
}

Pruebas
? Mismo ejemplo; salida 9 y lista de índices seleccionados.