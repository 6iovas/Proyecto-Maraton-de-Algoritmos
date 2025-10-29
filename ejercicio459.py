// Proyecto de Informatica
// Ejercicio 459
Título del Ejercicio: Sumar Elementos de Array Recursivamente
Análisis del Problema
? Descripción del Problema: Calcular la suma de todos los elementos de un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Suma de elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño=0 ? retornar 0.

2. Retornar primer elemento + suma del resto del array.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main() y sumaRecursiva().

Código Fuente (C++)
#include <iostream>
using namespace std;

int sumaRecursiva(int arr[], int n){
    if(n==0) return 0;
    return arr[0] + sumaRecursiva(arr+1,n-1);
}

int main() {
    int arr[]={1,2,3,4,5}, n=5;
    cout << "Suma: " << sumaRecursiva(arr,n) << endl; // 15
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? 15

? Caso 2: [0,0,0] ? 0

? Caso 3: [] ? 0