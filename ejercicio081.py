// Proyecto de Informatica
// Ejercicio 81
Título del Ejercicio: Secuencia Común Más Larga
Análisis del Problema
? Descripción del Problema: Dadas dos cadenas, encontrar la longitud de su subsecuencia común más larga.

? Entradas y Salidas:

? Entrada: Dos cadenas s1 y s2.

? Salida: Longitud del LCS.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear matriz dp[m+1][n+1].

2. Llenar dp[i][j] usando regla: si s1[i-1]==s2[j-1] entonces dp[i][j]=dp[i-1][j-1]+1, else max(dp[i-1][j],dp[i][j-1]).

3. Mostrar dp[m][n].

? Estructuras de Datos: Array 2D dp.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
using namespace std;

int main(){
    string s1,s2;
    cout<<"Ingrese dos cadenas: ";
    cin>>s1>>s2;
    int m=s1.size(), n=s2.size();
    vector<vector<int>> dp(m+1,vector<int>(n+1,0));

    for(int i=1;i<=m;i++){
        for(int j=1;j<=n;j++){
            if(s1[i-1]==s2[j-1]) dp[i][j]=dp[i-1][j-1]+1;
            else dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
        }
    }

    cout<<"Longitud del LCS: "<<dp[m][n]<<endl;
    return 0;
}

Pruebas:
? Caso 1: "AGGTAB" y "GXTXAYB" ? Salida: 4 (GTAB)
80. Longest Increasing Subsequence (LIS)