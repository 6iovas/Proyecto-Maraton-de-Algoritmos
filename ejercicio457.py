// Proyecto de Informatica
// Ejercicio 457
Título del Ejercicio: Buscar Valor Mínimo Recursivamente
Análisis del Problema
? Descripción del Problema: Encontrar el valor mínimo de un array usando recursión.

? Entradas y Salidas:

? Entrada: Array de enteros y tamaño.

? Salida: Valor mínimo.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si tamaño=1 ? retornar el único valor.

2. Comparar primer elemento con mínimo del resto del array.

? Estructuras de Datos: Array de enteros.

? Funciones Principales: main() y minRecursivo().

Código Fuente (C++)
#include <iostream>
using namespace std;

int minRecursivo(int arr[], int n){
    if(n==1) return arr[0];
    int minR= minRecursivo(arr+1,n-1);
    return (arr[0]<minR)?arr[0]:minR;
}

int main() {
    int arr[]={4,2,9,1,5}, n=5;
    cout << "Minimo: " << minRecursivo(arr,n) << endl; // 1
    return 0;
}

Pruebas
? Caso 1: [4,2,9,1,5] ? 1

? Caso 2: [1,2,3] ? 1

? Caso 3: [7] ? 7