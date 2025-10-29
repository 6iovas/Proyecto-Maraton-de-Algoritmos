// Proyecto de Informatica
// Ejercicio 491
Título del Ejercicio: Encontrar Índice de Número en Array
Análisis del Problema
? Descripción del Problema: Retornar el índice de la primera aparición de un número en un array.

? Entradas y Salidas:

? Entrada: Array de enteros, tamaño y número x.

? Salida: Índice si existe, -1 si no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer array y comparar cada elemento con x.

2. Retornar índice si se encuentra; -1 si no.

? Estructuras de Datos: Array de enteros y variable índice.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={5,3,7,3}, n=4, x=3;
    int indice=-1;
    for(int i=0;i<n;i++){
        if(arr[i]==x){indice=i; break;}
    }
    cout << "Indice de " << x << ": " << indice << endl; // 1
    return 0;
}

Pruebas
? Caso 1: [5,3,7,3], x=3 ? 1

? Caso 2: [1,2,3], x=4 ? -1

? Caso 3: [7,8,9], x=7 ? 0