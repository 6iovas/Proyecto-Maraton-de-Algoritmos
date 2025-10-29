// Proyecto de Informatica
// Ejercicio 337
Título del Ejercicio: Invertir Array
Análisis del Problema
? Descripción del Problema: Invertir los elementos de un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Array invertido.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar dos punteros: inicio y fin.

2. Intercambiar elementos hasta que inicio ? fin.

3. Mostrar array invertido.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1,2,3,4,5};
    int n=5;

    for(int i=0,j=n-1;i<j;i++,j--) {
        int temp = arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    cout << "Array invertido: ";
    for(int i=0;i<n;i++) cout << arr[i] << " ";
    cout << endl;
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5] ? [5,4,3,2,1]

? Caso 2: [10,20,30] ? [30,20,10]

? Caso 3: [1] ? [1]