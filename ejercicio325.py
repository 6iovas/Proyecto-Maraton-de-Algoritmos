// Proyecto de Informatica
// Ejercicio 325
Título del Ejercicio: Buscar Elemento en Array Ordenado (Búsqueda Binaria Recursiva)
Análisis del Problema
? Descripción del Problema: Implementar búsqueda binaria recursiva en un array ordenado.

? Entradas y Salidas:

? Entrada: Array ordenado y valor a buscar.

? Salida: Posición del elemento o -1 si no existe.

Diseño de la Solución
? Algoritmo Propuesto:

1. Determinar elemento medio.

2. Si coincide, retornar índice.

3. Si menor ? buscar mitad izquierda; si mayor ? mitad derecha.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main() y busquedaBinRec().

Código Fuente (C++)
#include <iostream>
using namespace std;

int busquedaBinRec(int arr[], int izquierda, int derecha, int x) {
    if(izquierda > derecha) return -1;
    int medio = izquierda + (derecha - izquierda)/2;
    if(arr[medio] == x) return medio;
    if(arr[medio] > x) return busquedaBinRec(arr, izquierda, medio-1, x);
    return busquedaBinRec(arr, medio+1, derecha, x);
}

int main() {
    int arr[] = {1,3,5,7,9};
    int n = 5, x=7;
    int pos = busquedaBinRec(arr,0,n-1,x);
    cout << "Posicion de " << x << ": " << pos << endl; // 3
    return 0;
}

Pruebas
? Caso 1: Buscar 7 ? 3

? Caso 2: Buscar 1 ? 0

? Caso 3: Buscar 10 ? -1