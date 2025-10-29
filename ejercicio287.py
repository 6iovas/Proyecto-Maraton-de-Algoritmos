// Proyecto de Informatica
// Ejercicio 287
Título del Ejercicio: Factorial de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular el factorial de un número entero n usando recursión. Por ejemplo, si n = 4, el resultado es 4 * 3 * 2 * 1 = 24.

? Entradas y Salidas:

? Entrada: Un número entero n (no negativo).

? Salida: Factorial de n.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir al usuario un número entero n.

2. Crear una función recursiva que devuelva 1 si n = 0 o 1.

3. Si n > 1, retornar n * factorial(n - 1).

4. Mostrar el resultado.

? Estructuras de Datos: Variable entera para n y resultado.

? Funciones Principales: main() y factorial(int n).

Código Fuente (C++)
#include <iostream>

int factorial(int n) {
    if (n <= 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int n;
    std::cout << "Ingresa un numero entero no negativo: ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "Error: el numero debe ser no negativo." << std::endl;
        return 1;
    }

    std::cout << "El factorial de " << n << " es: " << factorial(n) << std::endl;
    return 0;
}

Pruebas
? Caso 1: n = 4 ? Salida: 24

? Caso 2: n = 0 ? Salida: 1

? Caso 3: n = 5 ? Salida: 120