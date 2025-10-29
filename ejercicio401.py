// Proyecto de Informatica
// Ejercicio 401
Título del Ejercicio: Sumar Dos Números con Punteros
Análisis del Problema
? Descripción del Problema: Sumar dos números usando punteros.

? Entradas y Salidas:

? Entrada: Dos números enteros.

? Salida: Suma de ambos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear punteros a los números.

2. Calcular suma usando punteros.

? Estructuras de Datos: Variables enteras y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int a=5, b=7;
    int *pa=&a, *pb=&b;
    int suma = *pa + *pb;
    cout << "Suma: " << suma << endl; // 12
    return 0;
}

Pruebas
? Caso 1: 5 + 7 ? 12

? Caso 2: 0 + 0 ? 0

? Caso 3: -3 + 3 ? 0