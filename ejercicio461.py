// Proyecto de Informatica
// Ejercicio 461
Título del Ejercicio: Invertir Array Recursivamente
Análisis del Problema
? Descripción del Problema: Invertir los elementos de un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Array invertido.

Diseño de la Solución
? Algoritmo Propuesto:

1. Intercambiar primer y último elemento.

2. Llamar recursivamente al sub-array interno.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main() y invertirRecursivo().

Código Fuente (C++)
#include <iostream>
using namespace std;

void invertirRecursivo(int arr[], int start, int end){
    if(start>=end) return;
    swap(arr[start], arr[end]);
    invertirRecursivo(arr, start+1, end-1);
}

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    invertirRecursivo(arr,0,n-1);
    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl; // 5 4 3 2 1
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? [5,4,3,2,1]

? Caso 2: [1,2] ? [2,1]

? Caso 3: [7] ? [7]