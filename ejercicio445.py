// Proyecto de Informatica
// Ejercicio 445
Título del Ejercicio: Sumar Diagonal de Matriz
Análisis del Problema
? Descripción del Problema: Calcular la suma de los elementos de la diagonal principal de una matriz cuadrada.

? Entradas y Salidas:

? Entrada: Matriz cuadrada n x n.

? Salida: Suma de la diagonal.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la matriz solo usando índice i para mat[i][i].

2. Acumular los valores en una variable suma.

? Estructuras de Datos: Matriz y variable suma.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[3][3]={{1,2,3},{4,5,6},{7,8,9}};
    int suma=0, n=3;

    for(int i=0;i<n;i++)
        suma+=mat[i][i];

    cout << "Suma de diagonal: " << suma << endl; // 15
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6],[7,8,9]] ? 15

? Caso 2: [[2,0],[0,3]] ? 5

? Caso 3: [[1]] ? 1