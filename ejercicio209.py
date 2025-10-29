// Proyecto de Informatica
// Ejercicio 209
Dado n objetos con peso w[i] y valor v[i] y capacidad W, encontrar valor máximo y el subconjunto de índices escogidos. Debe entregar tanto el valor óptimo como la lista de elementos seleccionados. Usar DP O(nW) (n hasta ~200, W hasta ~1e4 en ejercicios prácticos).
Diseño de la solución
? DP 2D dp[i][cap] (i objetos considerados) con reconstrucción: si dp[i][cap] != dp[i-1][cap] entonces objeto i-1 fue tomado.

? Para ahorrar memoria, podríamos usar 1D y reconstrucción con tracking, pero 2D más simple para enseñar la técnica.

Código (C++)
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, W; 
    if(!(cin>>n>>W)) return 0;
    vector<int> w(n), v(n);
    for(int i=0;i<n;++i) cin>>w[i]>>v[i];
    vector<vector<int>> dp(n+1, vector<int>(W+1, 0));
    for(int i=1;i<=n;++i){
        for(int cap=0; cap<=W; ++cap){
            dp[i][cap] = dp[i-1][cap];
            if(cap >= w[i-1]) dp[i][cap] = max(dp[i][cap], dp[i-1][cap - w[i-1]] + v[i-1]);
        }
    }
    int best = dp[n][W];
    cout << "Valor optimo: " << best << "\n";
    // reconstrucción
    int cap = W;
    vector<int> chosen;
    for(int i=n;i>=1;--i){
        if(dp[i][cap] != dp[i-1][cap]){
            chosen.push_back(i-1); // tomar objeto i-1
            cap -= w[i-1];
        }
    }
    reverse(chosen.begin(), chosen.end());
    cout << "Objetos elegidos (indices 0-based):";
    for(int idx: chosen) cout << ' ' << idx;
    cout << '\n';
    return 0;
}

Pruebas
Entrada:

 4 7
1 1
3 4
4 5
5 7
?  Salida: Valor optimo: 9 y Objetos elegidos: 1 2 (ó los índices que correspondan).