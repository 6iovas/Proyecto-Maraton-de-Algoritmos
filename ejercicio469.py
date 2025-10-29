// Proyecto de Informatica
// Ejercicio 469
Título del Ejercicio: Eliminar Duplicados en Array
Análisis del Problema
? Descripción del Problema: Eliminar elementos duplicados de un array.

? Entradas y Salidas:

? Entrada: Array de enteros.

? Salida: Array sin duplicados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer el array y agregar a un nuevo array solo si no existe.

2. Mostrar array resultante.

? Estructuras de Datos: Array original y array resultante.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,2,3,4,4,5}, n=7, res[7], k=0;
    for(int i=0;i<n;i++){
        bool duplicado=false;
        for(int j=0;j<k;j++)
            if(arr[i]==res[j]) duplicado=true;
        if(!duplicado) res[k++]=arr[i];
    }
    for(int i=0;i<k;i++) cout << res[i] << " ";
    cout << endl; // 1 2 3 4 5
    return 0;
}

Pruebas
? Caso 1: [1,2,2,3] ? [1,2,3]

? Caso 2: [5,5,5] ? [5]

? Caso 3: [1,2,3] ? [1,2,3]