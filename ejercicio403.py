// Proyecto de Informatica
// Ejercicio 403
Título del Ejercicio: Intercambiar Valores con Punteros
Análisis del Problema
? Descripción del Problema: Intercambiar los valores de dos variables usando punteros.

? Entradas y Salidas:

? Entrada: Dos números enteros.

? Salida: Valores intercambiados.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear punteros a las variables.

2. Usar variable temporal para intercambiar.

? Estructuras de Datos: Variables enteras y punteros.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int a=10, b=20;
    int *pa=&a, *pb=&b;
    int temp = *pa;
    *pa = *pb;
    *pb = temp;
    cout << "a=" << a << ", b=" << b << endl; // a=20, b=10
    return 0;
}

Pruebas
? Caso 1: 10 y 20 ? a=20, b=10

? Caso 2: -5 y 5 ? a=5, b=-5

? Caso 3: 0 y 0 ? a=0, b=0