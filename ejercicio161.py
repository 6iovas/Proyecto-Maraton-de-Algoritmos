// Proyecto de Informatica
// Ejercicio 161
Ejercicio 158: Calcular número de caminos en una cuadrícula (DP)
Análisis del Problema
 En una cuadrícula m x n, calcular cuántas rutas existen desde la esquina superior izquierda hasta la inferior derecha moviéndose solo hacia la derecha o abajo.
Diseño de la Solución
 Usar programación dinámica:
 dp[i][j] = dp[i-1][j] + dp[i][j-1].
Código Fuente (C++)
#include <bits/stdc++.h>
using namespace std;

int main(){
    int m,n; cin>>m>>n;
    vector<vector<long long>> dp(m, vector<long long>(n,1));
    for(int i=1;i<m;++i)
        for(int j=1;j<n;++j)
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
    cout<<"Número de caminos: "<<dp[m-1][n-1]<<"\n";
}

Pruebas
? Entrada: 3 3

? Salida: Número de caminos: 6