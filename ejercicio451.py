// Proyecto de Informatica
// Ejercicio 451
Título del Ejercicio: Sumar Números Pares en Array
Análisis del Problema
? Descripción del Problema: Calcular la suma de los números pares de un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Suma de los números pares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar suma=0.

2. Recorrer array y sumar solo los números pares.

? Estructuras de Datos: Array de enteros y variable suma.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,5,6}, n=6, suma=0;
    for(int i=0;i<n;i++)
        if(arr[i]%2==0) suma+=arr[i];
    cout << "Suma pares: " << suma << endl; // 12
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5,6] ? 12

? Caso 2: [1,3,5] ? 0

? Caso 3: [2,4,6,8] ? 20