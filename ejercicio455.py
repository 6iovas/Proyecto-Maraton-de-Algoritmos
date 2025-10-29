// Proyecto de Informatica
// Ejercicio 455
Título del Ejercicio: Buscar Valor Máximo Recursivamente
Análisis del Problema
? Descripción del Problema: Encontrar el valor máximo de un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Valor máximo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño=1 ? retornar el único valor.

2. Comparar primer elemento con máximo del resto del array.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main() y maxRecursivo().

Código Fuente (C++)
#include <iostream>
using namespace std;

int maxRecursivo(int arr[], int n){
    if(n==1) return arr[0];
    int maxR= maxRecursivo(arr+1,n-1);
    return (arr[0]>maxR)?arr[0]:maxR;
}

int main() {
    int arr[]={1,7,3,9,5}, n=5;
    cout << "Maximo: " << maxRecursivo(arr,n) << endl; // 9
    return 0;
}

Pruebas
? Caso 1: [1,7,3,9,5