// Proyecto de Informatica
// Ejercicio 80
Título del Ejercicio: Subset Sum usando DP
Análisis del Problema
? Descripción del Problema: Determinar si existe un subconjunto de un conjunto de enteros que sume un valor S.

? Entradas y Salidas:

? Entrada: Número de elementos n, elementos del conjunto, suma objetivo S.

? Salida: Sí si existe un subconjunto que suma S, No si no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear tabla dp[n+1][S+1] donde dp[i][j] indica si suma j es posible con primeros i elementos.

2. Inicializar dp[i][0]=true.

3. Llenar tabla según inclusión/exclusión.

4. Mostrar resultado dp[n][S].

? Estructuras de Datos: Array 2D dp.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n,S;
    cout<<"Ingrese número de elementos y suma objetivo: ";
    cin>>n>>S;
    vector<int> arr(n);
    cout<<"Ingrese elementos:\n";
    for(int i=0;i<n;i++) cin>>arr[i];

    vector<vector<bool>> dp(n+1,vector<bool>(S+1,false));
    for(int i=0;i<=n;i++) dp[i][0]=true;

    for(int i=1;i<=n;i++){
        for(int j=1;j<=S;j++){
            if(arr[i-1]<=j) dp[i][j]=dp[i-1][j] || dp[i-1][j-arr[i-1]];
            else dp[i][j]=dp[i-1][j];
        }
    }

    if(dp[n][S]) cout<<"Sí, existe un subconjunto que suma "<<S<<endl;
    else cout<<"No, no existe un subconjunto que suma "<<S<<endl;

    return 0;
}

Pruebas:
? Caso 1: [3 34 4 12 5 2], S=9 ? Salida: Sí (4+5)
79. Longest Common Subsequence (LCS)