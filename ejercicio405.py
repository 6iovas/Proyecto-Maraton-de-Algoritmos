// Proyecto de Informatica
// Ejercicio 405
Título del Ejercicio: Calcular Máximo de un Array
Análisis del Problema
? Descripción del Problema: Encontrar el valor máximo dentro de un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros y su tamaño.

? Salida: Valor máximo encontrado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar max con el primer elemento del array.

2. Recorrer el array comparando cada elemento con max.

3. Actualizar max si se encuentra un valor mayor.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={3,7,2,9,5}, n=5;
    int max=arr[0];

    for(int i=1;i<n;i++)
        if(arr[i]>max) max=arr[i];

    cout << "Maximo valor: " << max << endl; // 9
    return 0;
}

Pruebas
? Caso 1: [3,7,2,9,5] ? 9

? Caso 2: [1,1,1] ? 1

? Caso 3: [5] ? 5