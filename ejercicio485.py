// Proyecto de Informatica
// Ejercicio 485
Título del Ejercicio: Ordenar Array Ascendente (Burbuja)
Análisis del Problema
? Descripción del Problema: Ordenar un array en orden ascendente usando el método burbuja.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Array ordenado ascendente.

Diseño de la Solución
? Algoritmo Propuesto:

1. Comparar elementos consecutivos.

2. Intercambiar si el anterior > siguiente.

3. Repetir hasta ordenar todo el array.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={5,2,8,1,3}, n=5;
    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-i-1;j++)
            if(arr[j]>arr[j+1]) swap(arr[j],arr[j+1]);
    for(int i=0;i<n;i++) cout << arr[i] << " "; // 1 2 3 5 8
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [5,2,8,1,3] ? [1,2,3,5,8]

? Caso 2: [1,2,3] ? [1,2,3]

? Caso 3: [3,2,1] ? [1,2,3]