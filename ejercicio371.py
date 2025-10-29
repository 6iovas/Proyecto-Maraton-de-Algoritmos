// Proyecto de Informatica
// Ejercicio 371
Título del Ejercicio: Potencia de un Número (Recursivo)
Análisis del Problema
? Descripción del Problema: Calcular la potencia base^exponente usando recursión.

? Entradas y Salidas:

? Entrada: Enteros base y exponente (?0).

? Salida: Resultado de base^exponente.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si exponente == 0 ? retornar 1.

2. Retornar base * potencia(base, exponente-1).

? Estructuras de Datos: Variables enteras.

? Funciones Principales: main() y potencia().

Código Fuente (C++)
#include <iostream>
using namespace std;

int potencia(int base, int exp) {
    if(exp==0) return 1;
    return base * potencia(base, exp-1);
}

int main() {
    int base=2, exp=5;
    cout << base << "^" << exp << " = " << potencia(base, exp) << endl; // 32
    return 0;
}

Pruebas
? Caso 1: base=2, exp=5 ? 32

? Caso 2: base=3, exp=0 ? 1

? Caso 3: base=5, exp=3 ? 125