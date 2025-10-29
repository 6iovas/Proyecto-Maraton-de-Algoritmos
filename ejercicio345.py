// Proyecto de Informatica
// Ejercicio 345
Título del Ejercicio: Buscar Mínimo en un Array
Análisis del Problema
? Descripción del Problema: Encontrar el valor mínimo de un array de enteros.

? Entradas y Salidas:

? Entrada: Array y su tamaño.

? Salida: Valor mínimo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar mínimo con primer elemento.

2. Recorrer array comparando y actualizando mínimo.

3. Mostrar resultado.

? Estructuras de Datos: Array y variable mínimo.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[] = {5,10,3,8,20};
    int n=5;
    int minimo=arr[0];

    for(int i=1;i<n;i++)
        if(arr[i]<minimo) minimo=arr[i];

    cout << "Minimo: " << minimo << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [5,10,3,8,20] ? 3

? Caso 2: [1,2,3] ? 1

? Caso 3: [10,10,10] ? 10