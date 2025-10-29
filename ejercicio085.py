// Proyecto de Informatica
// Ejercicio 85
Título del Ejercicio: Problema de Monedas
Análisis del Problema
? Descripción del Problema: Dado un conjunto de monedas y un valor S, contar el número de formas de obtener S.

? Entradas y Salidas:

? Entrada: Número de tipos de monedas n, valor de cada moneda, suma objetivo S.

? Salida: Número de formas de obtener S.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear vector dp[S+1] inicializado en 0, dp[0]=1.

2. Para cada moneda c, actualizar dp[j]+=dp[j-c] para j>=c.

3. Mostrar dp[S].

? Estructuras de Datos: vector<int> dp.

? Funciones Principales: main.

Código Fuente (C++):
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n,S;
    cout<<"Ingrese número de monedas y suma objetivo: ";
    cin>>n>>S;
    vector<int> monedas(n);
    cout<<"Ingrese valores de monedas:\n";
    for(int i=0;i<n;i++) cin>>monedas[i];

    vector<int> dp(S+1,0); dp[0]=1;
    for(int c: monedas)
        for(int j=c;j<=S;j++) dp[j]+=dp[j-c];

    cout<<"Número de formas de obtener "<<S<<": "<<dp[S]<<endl;
    return 0;
}

Pruebas:
? Caso 1: Monedas [1,2,5], S=5 ? Salida: 4
84. Usar std::set para mantener números únicos y ordenados