// Proyecto de Informatica
// Ejercicio 301
Título del Ejercicio: Calcular Potencia de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Crear una función recursiva que calcule la potencia de un número base elevado a un exponente n. Por ejemplo, 2^3 = 8.

? Entradas y Salidas:

? Entrada: Número base y exponente n (entero no negativo).

? Salida: Resultado de base^n.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir al usuario base y n.

2. Crear función recursiva potencia(base, n) que retorne 1 si n=0, o base * potencia(base, n-1).

3. Mostrar el resultado.

? Estructuras de Datos: Variables enteras para base, exponente y resultado.

? Funciones Principales: main() y potencia().

Código Fuente (C++)
#include <iostream>

int potencia(int base, int n) {
    if(n == 0) return 1;
    return base * potencia(base, n-1);
}

int main() {
    int base, n;
    std::cout << "Ingresa la base: ";
    std::cin >> base;
    std::cout << "Ingresa el exponente (entero no negativo): ";
    std::cin >> n;

    if(n < 0) {
        std::cout << "Error: El exponente debe ser no negativo." << std::endl;
        return 1;
    }

    std::cout << base << "^" << n << " = " << potencia(base, n) << std::endl;
    return 0;
}

Pruebas
? Caso 1: base=2, n=3 ? Salida: 8

? Caso 2: base=5, n=0 ? Salida: 1

? Caso 3: base=3, n=4 ? Salida: 81