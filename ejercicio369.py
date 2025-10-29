// Proyecto de Informatica
// Ejercicio 369
Título del Ejercicio: Factorial de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular el factorial de un número entero usando recursión.

? Entradas y Salidas:

? Entrada: Número entero positivo n.

? Salida: Factorial de n.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si n == 0 o n == 1 ? retornar 1.

2. Retornar n * factorial(n-1).

? Estructuras de Datos: Variable entera.

? Funciones Principales: main() y factorial().

Código Fuente (C++)
#include <iostream>
using namespace std;

int factorial(int n) {
    if(n<=1) return 1;
    return n * factorial(n-1);
}

int main() {
    int n=5;
    cout << "Factorial de " << n << " es " << factorial(n) << endl; // 120
    return 0;
}

Pruebas
? Caso 1: n=5 ? 120

? Caso 2: n=0 ? 1

? Caso 3: n=1 ? 1