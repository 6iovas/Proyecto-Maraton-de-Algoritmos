// Proyecto de Informatica
// Ejercicio 373
Título del Ejercicio: Ordenar un Array Ascendentemente
Análisis del Problema
? Descripción del Problema: Ordenar los elementos de un array de enteros de menor a mayor usando el algoritmo de burbuja.

? Entradas y Salidas:

? Entrada: Array de enteros y su tamaño.

? Salida: Array ordenado ascendentemente.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer el array con bucles anidados.

2. Comparar elementos adyacentes y permutarlos si es necesario.

3. Mostrar el array ordenado.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[] = {5,2,9,1,5};
    int n = 5;

    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-i-1;j++)
            if(arr[j]>arr[j+1])
                swap(arr[j], arr[j+1]);

    cout << "Array ordenado: ";
    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [5,2,9,1,5] ? [1,2,5,5,9]

? Caso 2: [3,1] ? [1,3]

? Caso 3: [1,2,3] ? [1,2,3]