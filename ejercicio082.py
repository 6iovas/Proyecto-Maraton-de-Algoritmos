// Proyecto de Informatica
// Ejercicio 82
Título del Ejercicio: Subsequence Creciente Más Larga
Análisis del Problema
? Descripción del Problema: Dado un array, encontrar la longitud de la subsecuencia creciente más larga.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Longitud de la LIS.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear vector dp con 1 para cada elemento.

2. Para cada elemento, actualizar dp[i]=max(dp[i], dp[j]+1) si arr[i]>arr[j].

3. Mostrar max(dp).

? Estructuras de Datos: vector<int> para dp.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cout<<"Ingrese tamaño del array: ";
    cin>>n;
    vector<int> arr(n);
    cout<<"Ingrese elementos:\n";
    for(int i=0;i<n;i++) cin>>arr[i];

    vector<int> dp(n,1);
    for(int i=1;i<n;i++){
        for(int j=0;j<i;j++){
            if(arr[i]>arr[j]) dp[i]=max(dp[i],dp[j]+1);
        }
    }

    cout<<"Longitud de la LIS: "<<*max_element(dp.begin(),dp.end())<<endl;
    return 0;
}

Pruebas:
? Caso 1: [10,22,9,33,21,50,41,60] ? Salida: 5 (10,22,33,50,60)

81. Floyd-Warshall para Todas las Distancias Mínimas