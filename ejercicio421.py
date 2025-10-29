// Proyecto de Informatica
// Ejercicio 421
Título del Ejercicio: Sumar Dos Matrices
Análisis del Problema
? Descripción del Problema: Sumar dos matrices del mismo tamaño.

? Entradas y Salidas:

? Entrada: Dos matrices m x n.

? Salida: Matriz resultante.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer ambas matrices y sumar elementos correspondientes.

2. Mostrar matriz resultante.

? Estructuras de Datos: Matrices bidimensionales.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int A[2][2]={{1,2},{3,4}};
    int B[2][2]={{5,6},{7,8}};
    int C[2][2];

    for(int i=0;i<2;i++)
        for(int j=0;j<2;j++)
            C[i][j]=A[i][j]+B[i][j];

    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++) cout << C[i][j] << " ";
        cout