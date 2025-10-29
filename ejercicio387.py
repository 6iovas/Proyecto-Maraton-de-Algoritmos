// Proyecto de Informatica
// Ejercicio 387
Título del Ejercicio: Imprimir Tabla de Multiplicar
Análisis del Problema
? Descripción del Problema: Imprimir la tabla de multiplicar de un número.

? Entradas y Salidas:

? Entrada: Número entero n.

? Salida: Tabla de multiplicar del 1 al 10.

Diseño de la Solución
? Algoritmo Propuesto:

1. Pedir número n.

2. Usar bucle de 1 a 10 y multiplicar n*i.

3. Mostrar resultados.

? Estructuras de Datos: Variable entera.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int n=5;
    for(int i=1;i<=10;i++)
        cout << n << " x " << i << " = " << n*i << endl;
    return 0;
}

Pruebas
? Caso 1: n=5 ? 5x1=5 ... 5x10=50

? Caso 2: n=3 ? 3x1=3 ... 3x10=30

? Caso 3: n=0 ? todos 0