// Proyecto de Informatica
// Ejercicio 391
Título del Ejercicio: Sumar Elementos de Array Dinámico
Análisis del Problema
? Descripción del Problema: Crear un array dinámico y sumar sus elementos.

? Entradas y Salidas:

? Entrada: Tamaño n y elementos del array.

? Salida: Suma de elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir tamaño del array.

2. Crear array dinámico new int[n].

3. Recorrer array y acumular suma.

? Estructuras de Datos: Array dinámico y variable suma.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int n=4;
    int* arr = new int[n]{1,2,3,4};
    int suma=0;

    for(int i=0;i<n;i++) suma+=arr[i];

    cout << "Suma de elementos: " << suma << endl; // 10
    delete[] arr;
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4] ? 10

? Caso 2: [0,0,0] ? 0

? Caso 3: [5,10] ? 15