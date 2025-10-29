// Proyecto de Informatica
// Ejercicio 453
Título del Ejercicio: Contar Números Negativos en Array
Análisis del Problema
? Descripción del Problema: Contar cuántos números negativos hay en un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Cantidad de números negativos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer array y aumentar contador si el número es negativo.

? Estructuras de Datos: Array de enteros y variable contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={-1,2,-3,4,-5}, n=5, contador=0;
    for(int i=0;i<n;i++)
        if(arr[i]<0) contador++;
    cout << "Numeros negativos: " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [-1,2,-3,4,-5] ? 3

? Caso 2: [1,2,3] ? 0

? Caso 3: [-1,-2,-3] ? 3