// Proyecto de Informatica
// Ejercicio 285
Título del Ejercicio: Intercambio de Valores con Punteros
Análisis del Problema
? Descripción del Problema: Crear una función que reciba dos punteros a enteros y los intercambie. Por ejemplo, si a = 5 y b = 10, después del intercambio a = 10 y b = 5.

? Entradas y Salidas:

? Entrada: Dos números enteros a y b.

? Salida: Los valores intercambiados de a y b.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir al usuario que ingrese dos números enteros.

2. Llamar a una función que reciba punteros a los dos números.

3. Dentro de la función, usar una variable temporal para intercambiar los valores.

4. Mostrar los valores intercambiados.

? Estructuras de Datos: Dos variables enteras y un puntero por cada variable.

? Funciones Principales: main() y intercambiar(int* x, int* y).

Código Fuente (C++)
#include <iostream>

void intercambiar(int* x, int* y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main() {
    int a, b;
    std::cout << "Ingresa dos numeros enteros: ";
    std::cin >> a >> b;

    intercambiar(&a, &b);

    std::cout << "Valores intercambiados: a = " << a << ", b = " << b << std::endl;
    return 0;
}

Pruebas
? Caso 1: a = 5, b = 10 ? Salida: a = 10, b = 5

? Caso 2: a = -3, b = 7 ? Salida: a = 7, b = -3

? Caso 3: a = 0, b = 0 ? Salida: a = 0, b = 0