// Proyecto de Informatica
// Ejercicio 343
Título del Ejercicio: Contar Números Impares en un Array
Análisis del Problema
? Descripción del Problema: Contar cuántos números impares hay en un array de enteros.

? Entradas y Salidas:

? Entrada: Array de enteros y su tamaño.

? Salida: Cantidad de números impares.

Diseño de la Solución
? Algoritmo Propuesto:

1. Inicializar contador en 0.

2. Recorrer array, si elemento %2!=0 incrementar contador.

3. Mostrar resultado.

? Estructuras de Datos: Array y variable contador.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1,2,3,4,5,6};
    int n=6, contador=0;

    for(int i=0;i<n;i++)
        if(arr[i]%2!=0) contador++;

    cout << "Numeros impares: " << contador << endl; // 3
    return 0;
}

Pruebas
? Caso 1: [1,2,3,4,5,6] ? 3

? Caso 2: [2,4,6,8] ? 0

? Caso 3: [1,3,5] ? 3