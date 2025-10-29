// Proyecto de Informatica
// Ejercicio 395
Título del Ejercicio: Media de Elementos de Array
Análisis del Problema
? Descripción del Problema: Calcular la media aritmética de los elementos de un array.

? Entradas y Salidas:

? Entrada: Array y tamaño.

? Salida: Media como número decimal.

Diseño de la Solución
? Algoritmo Propuesto:

1. Sumar elementos del array.

2. Dividir suma entre tamaño.

3. Mostrar resultado.

? Estructuras de Datos: Array y variable suma.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={2,4,6,8}, n=4;
    double suma=0;

    for(int i=0;i<n;i++) suma+=arr[i];

    cout << "Media = " << suma/n << endl; // 5
    return 0;
}

Pruebas
? Caso 1: [2,4,6,8] ? 5

? Caso 2: [1,1,1] ? 1

? Caso 3: [5,10] ? 7.5