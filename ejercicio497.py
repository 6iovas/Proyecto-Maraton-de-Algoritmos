// Proyecto de Informatica
// Ejercicio 497
Título del Ejercicio: Contar Elementos Pares en Array
Análisis del Problema
? Descripción del Problema: Contar cuántos números pares existen en un array.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Cantidad de números pares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer el array y aumentar contador si el elemento %2==0.

? Estructuras de Datos: Array de enteros y variable contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5,6}, n=6, contador=0;
    for(int i=0;i<n;i++)
        if(arr[i]%2==0) contador++;
    cout << "Cantidad de numeros pares: " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5,6] ? 3

? Caso 2: [1,3,5] ? 0

? Caso 3: [2,4,6,8] ? 4