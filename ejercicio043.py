// Proyecto de Informatica
// Ejercicio 43
Ejercicio 41: Resolver el problema de la mochila (Knapsack 0/1)
Análisis del Problema
 Máximo valor con capacidad W, cada objeto 0/1.
Diseño de la Solución
 DP 2D dp[i][w] o optimizado 1D. Aquí 1D (space O(W)).
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, W; if(!(cin>>n>>W)) return 0;
    vector<int> w(n), v(n);
    for(int i=0;i<n;++i) cin>>w[i]>>v[i];
    vector<int> dp(W+1,0);
    for(int i=0;i<n;++i){
        for(int cap = W; cap>=w[i]; --cap){
            dp[cap] = max(dp[cap], dp[cap - w[i]] + v[i]);
        }
    }
    cout << dp[W] << "\n";
    return 0;
}

Pruebas
? Entrada ejemplo: 4 7 seguido de 1 1, 3 4, 4 5, 5 7 ? salida 9.