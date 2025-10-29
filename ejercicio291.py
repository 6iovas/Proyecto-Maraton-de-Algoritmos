// Proyecto de Informatica
// Ejercicio 291
Título del Ejercicio: Suma de los Elementos de un Array con Punteros
Análisis del Problema
? Descripción del Problema: Crear un programa que reciba un array de enteros y calcule la suma de sus elementos usando punteros.

? Entradas y Salidas:

? Entrada: Tamaño del array n y n números enteros.

? Salida: Suma de los elementos del array.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir al usuario el tamaño del array n.

2. Crear un array dinámico de tamaño n.

3. Llenar el array con los valores ingresados.

4. Usar un puntero para recorrer el array y sumar sus elementos.

5. Mostrar la suma.

? Estructuras de Datos: Array dinámico y puntero.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>

int main() {
    int n, suma = 0;
    std::cout << "Ingresa el tamaño del array: ";
    std::cin >> n;

    int* arr = new int[n];

    std::cout << "Ingresa " << n << " numeros enteros:\n";
    for(int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    int* ptr = arr;
    for(int i = 0; i < n; ++i) {
        suma += *(ptr + i);
    }

    std::cout << "La suma de los elementos es: " << suma << std::endl;

    delete[] arr;
    return 0;
}

Pruebas
? Caso 1: n=3, array = [1,2,3] ? Salida: 6

? Caso 2: n=5, array = [2,4,6,8,10] ? Salida: 30

? Caso 3: n=0, array = [] ? Salida: 0