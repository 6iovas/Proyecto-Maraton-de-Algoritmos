// Proyecto de Informatica
// Ejercicio 377
Título del Ejercicio: Suma de Matriz
Análisis del Problema
? Descripción del Problema: Sumar todos los elementos de una matriz.

? Entradas y Salidas:

? Entrada: Matriz m x n.

? Salida: Suma de todos los elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Recorrer la matriz con bucles anidados.

2. Acumular todos los elementos en una variable suma.

3. Mostrar resultado.

? Estructuras de Datos: Matriz bidimensional y variable suma.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int mat[2][3]={{1,2,3},{4,5,6}};
    int suma=0;

    for(int i=0;i<2;i++)
        for(int j=0;j<3;j++)
            suma += mat[i][j];

    cout << "Suma de elementos de la matriz: " << suma << endl; // 21
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? 21

? Caso 2: [[0]] ? 0

? Caso 3: [[1,1],[1,1]] ? 4