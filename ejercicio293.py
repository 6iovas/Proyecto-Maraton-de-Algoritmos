// Proyecto de Informatica
// Ejercicio 293
Título del Ejercicio: Inversión de un Array Recursivamente
Análisis del Problema
? Descripción del Problema: Invertir un array de enteros usando recursión. Por ejemplo, [1,2,3] ? [3,2,1].

? Entradas y Salidas:

? Entrada: Tamaño n y n números enteros.

? Salida: Array invertido.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir tamaño y elementos del array.

2. Crear función recursiva invertir(int arr[], int inicio, int fin) que intercambie elementos extremos hasta el centro.

3. Mostrar array invertido.

? Estructuras de Datos: Array y variables enteras.

? Funciones Principales: main() y invertir().

Código Fuente (C++)
#include <iostream>

void invertir(int arr[], int inicio, int fin) {
    if(inicio >= fin) return;
    int temp = arr[inicio];
    arr[inicio] = arr[fin];
    arr[fin] = temp;
    invertir(arr, inicio+1, fin-1);
}

int main() {
    int n;
    std::cout << "Ingresa el tamaño del array: ";
    std::cin >> n;
    int arr[n];

    std::cout << "Ingresa los elementos del array:\n";
    for(int i=0; i<n; ++i) std::cin >> arr[i];

    invertir(arr, 0, n-1);

    std::cout << "Array invertido: ";
    for(int i=0; i<n; ++i) std::cout << arr[i] << " ";
    std::cout << std::endl;

    return 0;
}

Pruebas
? Caso 1: [1,2,3] ? [3,2,1]

? Caso 2: [5,10,15,20] ? [20,15,10,5]

? Caso 3: [7] ? [7]