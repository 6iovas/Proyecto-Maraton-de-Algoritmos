// Proyecto de Informatica
// Ejercicio 413
Título del Ejercicio: Invertir Array con Punteros
Análisis del Problema
? Descripción del Problema: Invertir los elementos de un array usando punteros.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Array invertido.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar punteros al inicio y al final del array.

2. Intercambiar valores hasta que los punteros se crucen.

? Estructuras de Datos: Array y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    int *start=arr, *end=arr+n-1;

    while(start<end){
        swap(*start,*end);
        start++; end--;
    }

    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl; // 5 4 3 2 1
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? [5,4,3,2,1]

? Caso 2: [1,2] ? [2,1]

? Caso 3: [1] ? [1]