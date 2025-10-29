// Proyecto de Informatica
// Ejercicio 467
Título del Ejercicio: Calcular Promedio de Array
Análisis del Problema
? Descripción del Problema: Calcular el promedio de los elementos de un array.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Promedio (float).

Diseño de la Solución
? Algoritmo Propuesto:

1. Sumar todos los elementos.

2. Dividir la suma entre el tamaño del array.

? Estructuras de Datos: Array de enteros y variable suma.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={2,4,6,8}, n=4, suma=0;
    for(int i=0;i<n;i++) suma+=arr[i];
    cout << "Promedio: " << (float)suma/n << endl; // 5
    return 0;
}

Pruebas
? Caso 1: [2,4,6,8] ? 5

? Caso 2: [1,1,1] ? 1

? Caso 3: [10,20] ? 15