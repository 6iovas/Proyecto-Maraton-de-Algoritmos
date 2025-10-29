// Proyecto de Informatica
// Ejercicio 477
Título del Ejercicio: Contar Elementos Mayores a X
Análisis del Problema
? Descripción del Problema: Contar cuántos elementos de un array son mayores a un valor x.

? Entradas y Salidas:

? Entrada: Array de enteros, tamaño n y valor x.

? Salida: Cantidad de elementos mayores que x.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer el array y aumentar contador si el elemento > x.

? Estructuras de Datos: Array de enteros y variable contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,5,3,7,2}, n=5, x=3, contador=0;
    for(int i=0;i<n;i++)
        if(arr[i]>x) contador++;
    cout << "Elementos mayores a " << x << ": " << contador << endl; // 2
    return 0;
}

Pruebas
? Caso 1: [1,5,3,7,2], x=3 ? 2

? Caso 2: [4,6,8], x=5 ? 2

? Caso 3: [1,2,3], x=10 ? 0