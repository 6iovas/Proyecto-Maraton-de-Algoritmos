// Proyecto de Informatica
// Ejercicio 335
Título del Ejercicio: Promedio de Array
Análisis del Problema
? Descripción del Problema: Calcular el promedio de los elementos de un array.

? Entradas y Salidas:

? Entrada: Array de enteros y su tamaño.

? Salida: Promedio de los elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Sumar todos los elementos del array.

2. Dividir entre cantidad de elementos.

3. Mostrar promedio.

? Estructuras de Datos: Array y variable suma.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[] = {5,10,15,20};
    int n=4;
    double suma=0;

    for(int i=0;i<n;i++) suma += arr[i];

    cout << "Promedio: " << suma/n << endl; // 12.5
    return 0;
}

Pruebas
? Caso 1: [5,10,15,20] ? 12.5

? Caso 2: [1,2,3] ? 2

? Caso 3: [10,10,10] ? 10