// Proyecto de Informatica
// Ejercicio 15
Ejercicio 15: Problema de la Mochila (0/1 Knapsack)
Análisis del Problema
 Maximizar el valor total de objetos con peso limitado.
Diseño de la Solución
1. Crear una matriz dp[n+1][W+1].

2. Llenarla comparando tomar o no cada objeto.

Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, W;
    cin >> n >> W;
    vector<int> w(n), v(n);
    for (int i = 0; i < n; i++) cin >> w[i] >> v[i];
    vector<vector<int>> dp(n+1, vector<int>(W+1));
    for (int i = 1; i <= n; i++) {
        for (int cap = 0; cap <= W; cap++) {
            dp[i][cap] = dp[i-1][cap];
            if (cap >= w[i-1])
                dp[i][cap] = max(dp[i][cap], dp[i-1][cap-w[i-1]] + v[i-1]);
        }
    }
    cout << dp[n][W];
}

Pruebas
Entrada:

 4 7
1 1
3 4
4 5
5 7
?  Salida: 9