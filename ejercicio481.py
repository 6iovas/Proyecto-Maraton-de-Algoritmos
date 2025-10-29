// Proyecto de Informatica
// Ejercicio 481
Título del Ejercicio: Contar Apariciones de Número
Análisis del Problema
? Descripción del Problema: Contar cuántas veces aparece un número específico en un array.

? Entradas y Salidas:

? Entrada: Array de enteros, tamaño y número x.

? Salida: Cantidad de apariciones de x.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador=0.

2. Recorrer array y aumentar contador si el elemento = x.

? Estructuras de Datos: Array de enteros y contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,2,4,2}, n=6, x=2, contador=0;
    for(int i=0;i<n;i++)
        if(arr[i]==x) contador++;
    cout << "El numero " << x << " aparece " << contador << " veces" << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,2,4,2], x=2 ? 3

? Caso 2: [1,1,1], x=1 ? 3

? Caso 3: [5,6,7], x=8 ? 0