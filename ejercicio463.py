// Proyecto de Informatica
// Ejercicio 463
Título del Ejercicio: Sumar Matriz Recursivamente
Análisis del Problema
? Descripción del Problema: Sumar todos los elementos de una matriz usando recursión.

? Entradas y Salidas:

? Entrada: Matriz m x n.

? Salida: Suma de todos los elementos.

Diseño de la Solución
? Algoritmo Propuesto:

1. Si la fila actual >= m ? retornar 0.

2. Sumar elementos de la fila actual + suma del resto de filas recursivamente.

? Estructuras de Datos: Matriz 2D y variable suma.

? Funciones Principales: main() y sumarMatrizRecursivo().

Código Fuente (C++)
#include <iostream>
using namespace std;

int sumarMatrizRecursivo(int mat[][3], int filas, int cols, int f=0){
    if(f>=filas) return 0;
    int sumaFila=0;
    for(int j=0;j<cols;j++) sumaFila+=mat[f][j];
    return sumaFila + sumarMatrizRecursivo(mat,filas,cols,f+1);
}

int main() {
    int mat[2][3]={{1,2,3},{4,5,6}};
    cout << "Suma matriz: " << sumarMatrizRecursivo(mat,2,3) << endl; // 21
    return 0;
}

Pruebas
? Caso 1: [[1,2,3],[4,5,6]] ? 21

? Caso 2: [[0]] ? 0

? Caso 3: [[1,1],[1,1]] ? 4