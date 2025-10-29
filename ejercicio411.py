// Proyecto de Informatica
// Ejercicio 411
Título del Ejercicio: Sumar Elementos de Matriz (Dinámica)
Análisis del Problema
? Descripción del Problema: Sumar todos los elementos de una matriz dinámica.

? Entradas y Salidas:

? Entrada: Matriz m x n.

? Salida: Suma de todos los elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Crear matriz dinámica con new.

2. Recorrer matriz y acumular suma.

3. Mostrar resultado y liberar memoria.

? Estructuras de Datos: Matriz dinámica.

? Funciones Principales: main().

Código Fuente (C++)
#include <iostream>
using namespace std;

int main() {
    int m=2,n=3;
    int** mat = new int*[m];
    for(int i=0;i<m;i++) mat[i]=new int[n]{1,2,3};

    int suma=0;
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            suma+=mat[i][j];

    cout << "Suma de matriz: " << suma << endl; // 12

    for(int i=0;i<m;i++) delete[] mat[i];
    delete[] mat;
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[1,2,3]] ? 12

? Caso 2: [[0]] ? 0

? Caso 3: [[1,1],[1,1]] ? 4