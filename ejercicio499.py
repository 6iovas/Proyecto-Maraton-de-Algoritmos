// Proyecto de Informatica
// Ejercicio 499
Título del Ejercicio: Contar Elementos Impares en Array
Análisis del Problema
? Descripción del Problema: Contar cuántos números impares existen en un array.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Cantidad de números impares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer array y aumentar contador si el elemento %2!=0.

? Estructuras de Datos: Array de enteros y variable contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5}, n=5, contador=0;
    for(int i=0;i<n;i++)
        if(arr[i]%2!=0) contador++;
    cout << "Cantidad de numeros impares: " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? 3

? Caso 2: [2,4,6] ? 0

? Caso 3: [1,3,5] ? 3