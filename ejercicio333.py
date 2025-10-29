// Proyecto de Informatica
// Ejercicio 333
Título del Ejercicio: Contar Elementos Mayores que un Valor en Array
Análisis del Problema
? Descripción del Problema: Contar cuántos elementos de un array son mayores que un valor dado.

? Entradas y Salidas:

? Entrada: Array de enteros y valor x.

? Salida: Número de elementos mayores que x.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador en 0.

2. Recorrer array, incrementar contador si elemento > x.

3. Mostrar contador.

? Estructuras de Datos: Array de enteros y variable contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[] = {5,10,3,8,20};
    int n=5, x=7, contador=0;

    for(int i=0;i<n;i++) if(arr[i]>x) contador++;

    cout << "Elementos mayores que " << x << ": " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [5,10,3,8,20], x=7 ? 3

? Caso 2: [1,2,3], x=0 ? 3

? Caso 3: [1,2,3], x=5 ? 0