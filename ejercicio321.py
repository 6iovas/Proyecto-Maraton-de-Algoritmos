// Proyecto de Informatica
// Ejercicio 321
Título del Ejercicio: Buscar el Máximo en un Array Recursivamente
Análisis del Problema
? Descripción del Problema: Crear una función recursiva que encuentre el valor máximo en un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros y su tamaño n.

? Salida: Valor máximo del array.

Diseño de la Solución
? Algoritmo Propuesto:

1. Definir función maxRec(arr, n) que retorne arr[0] si n==1.

2. Comparar último elemento con máximo de los anteriores recursivamente.

3. Retornar el máximo.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main() y maxRec().

Código Fuente (C++)
#include <iostream>
using namespace std;

int maxRec(int arr[], int n) {
    if(n == 1) return arr[0];
    int maxRest = maxRec(arr, n-1);
    return (arr[n-1] > maxRest) ? arr[n-1] : maxRest;
}

int main() {
    int arr[] = {5, 10, 3, 8, 20};
    int n = 5;
    cout << "Maximo del array: " << maxRec(arr, n) << endl; // 20
    return 0;
}

Pruebas
? Caso 1: [5,10,3,8,20] ? 20

? Caso 2: [1,2,3,4,5] ? 5

? Caso 3: [10,10,10] ? 10