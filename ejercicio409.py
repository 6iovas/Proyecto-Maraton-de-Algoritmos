// Proyecto de Informatica
// Ejercicio 409
Título del Ejercicio: Buscar Valor con Punteros
Análisis del Problema
? Descripción del Problema: Buscar un valor en un array usando punteros.

? Entradas y Salidas:

? Entrada: Array de enteros y valor x a buscar.

? Salida: Índice del valor o -1 si no se encuentra.

Diseño de la Solución
? Algoritmo Propuesto:

1. Usar un puntero para recorrer el array.

2. Comparar cada elemento con x.

3. Retornar índice si se encuentra; -1 si no.

? Estructuras de Datos: Array de enteros y puntero.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={10,20,30,40}, n=4, x=30;
    int* ptr=arr;
    int pos=-1;

    for(int i=0;i<n;i++){
        if(*(ptr+i)==x) pos=i;
    }

    cout << "Posicion de " << x << " = " << pos << endl; // 2
    return 0;
}

Pruebas
? Caso 1: [10,20,30,40], x=30 ? 2

? Caso 2: x=50 ? -1

? Caso 3: x=10 ? 0