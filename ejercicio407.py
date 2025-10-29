// Proyecto de Informatica
// Ejercicio 407
Título del Ejercicio: Calcular Mínimo de un Array
Análisis del Problema
? Descripción del Problema: Encontrar el valor mínimo dentro de un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros y su tamaño.

? Salida: Valor mínimo encontrado.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar min con el primer elemento del array.

2. Recorrer el array comparando cada elemento con min.

3. Actualizar min si se encuentra un valor menor.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={3,7,2,9,5}, n=5;
    int min=arr[0];

    for(int i=1;i<n;i++)
        if(arr[i]<min) min=arr[i];

    cout << "Minimo valor: " << min << endl; // 2
    return 0;
}

Pruebas
? Caso 1: [3,7,2,9,5] ? 2

? Caso 2: [1,1,1] ? 1

? Caso 3: [5] ? 5