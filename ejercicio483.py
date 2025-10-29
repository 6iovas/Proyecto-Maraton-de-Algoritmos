// Proyecto de Informatica
// Ejercicio 483
Título del Ejercicio: Generar Números Fibonacci Recursivos
Análisis del Problema
? Descripción del Problema: Calcular el n-ésimo número de Fibonacci usando recursión.

? Entradas y Salidas:

? Entrada: Entero n.

? Salida: n-ésimo número de Fibonacci.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si n=0 ? retornar 0

2. Si n=1 ? retornar 1

3. Si no ? fib(n-1) + fib(n-2)

? Estructuras de Datos: Entero y función recursiva.

? Funciones Principales: main() y fibonacci().

Código Fuente (C++)
#include <iostream>
using namespace std;

int fibonacci(int n){
    if(n==0) return 0;
    if(n==1) return 1;
    return fibonacci(n-1)+fibonacci(n-2);
}

int main() {
    int n=7;
    cout << "Fibonacci(" << n << ") = " << fibonacci(n) << endl; // 13
    return 0;
}

Pruebas
? Caso 1: n=0 ? 0

? Caso 2: n=7 ? 13

? Caso 3: n=10 ? 55