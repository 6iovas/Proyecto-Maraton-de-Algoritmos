// Proyecto de Informatica
// Ejercicio 489
Título del Ejercicio: Buscar Número en Array (Secuencial)
Análisis del Problema
? Descripción del Problema: Buscar si un número existe en un array usando búsqueda secuencial.

? Entradas y Salidas:

? Entrada: Array de enteros, tamaño y número x.

? Salida: true si existe, false si no.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer array y comparar cada elemento con x.

2. Retornar true si se encuentra; false si no.

? Estructuras de Datos: Array de enteros y variable bandera.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,4,6,8}, n=4, x=6;
    bool encontrado=false;
    for(int i=0;i<n;i++)
        if(arr[i]==x){encontrado=true; break;}
    if(encontrado) cout << x << " existe en el array" << endl;
    else cout << x << " no existe en el array" << endl;
    return 0;
}

Pruebas
? Caso 1: [1,4,6,8], x=6 ? existe

? Caso 2: [1,2,3], x=5 ? no existe

? Caso 3: [7,8,9], x=7 ? existe