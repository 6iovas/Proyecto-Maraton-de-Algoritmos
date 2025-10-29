// Proyecto de Informatica
// Ejercicio 473
Título del Ejercicio: Sumar Números Impares
Análisis del Problema
? Descripción del Problema: Calcular la suma de todos los números impares en un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Suma de números impares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer el array y sumar si el número es impar.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5}, n=5, suma=0;
    for(int i=0;i<n;i++) if(arr[i]%2!=0) suma+=arr[i];
    cout << "Suma impares: " << suma << endl; // 9
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? 9

? Caso 2: [2,4,6] ? 0

? Caso 3: [1,3,5] ? 9