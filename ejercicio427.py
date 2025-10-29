// Proyecto de Informatica
// Ejercicio 427
Título del Ejercicio: Recorrer Array Recursivamente
Análisis del Problema
? Descripción del Problema: Imprimir todos los elementos de un array usando recursión.

? Entradas y Salidas:

? Entrada: Array y tamaño.

? Salida: Elementos impresos en orden.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño == 0 ? retornar.

2. Imprimir primer elemento y llamar recursivamente al resto.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main() y imprimirArray().

Código Fuente (C++)
#include <iostream>
using namespace std;

void imprimirArray(int arr[], int n){
    if(n==0) return;
    cout << arr[0] << " ";
    imprimirArray(arr+1,n-1);
}

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    imprimirArray(arr,n); // 1 2 3 4 5
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,3] ? 1 2 3

? Caso 2: [5] ? 5

? Caso 3: [] ? (sin imprimir)